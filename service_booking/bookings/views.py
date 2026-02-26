from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Booking
from services.models import Service
from users.models import Profile
from django.db.models import Sum, Count
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def book_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        date = request.POST['date']
        time = request.POST['time']

        # 🚫 Prevent Double Booking
        if Booking.objects.filter(service=service, date=date, time=time).exists():
            messages.error(request, "This slot is already booked!")
            return redirect('book_service', service_id=service.id)

        Booking.objects.create(
            user=request.user,
            service=service,
            date=date,
            time=time
        )

        messages.success(request, "Booking successful!")
        return redirect('home')

    return render(request, 'book_service.html', {'service': service})

@login_required
def provider_dashboard(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('home')

    if profile.role != 'PROVIDER':
        return redirect('home')

    bookings = Booking.objects.filter(service__provider=request.user)

    return render(request, 'provider_dashboard.html', {'bookings': bookings})

@login_required
def update_booking_status(request, booking_id, status):
    booking = get_object_or_404(Booking, id=booking_id)

    if booking.service.provider != request.user:
        return redirect('home')

    booking.status = status
    booking.save()

    return redirect('provider_dashboard')

@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-date', '-time')
    return render(request, 'user_bookings.html', {'bookings': bookings})

@login_required
def payment_page(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if booking.is_paid:
        messages.info(request, "This booking is already paid.")
        return redirect('user_bookings')
    return render(request, 'payment.html', {'booking': booking})

@login_required
def process_payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        # Simulate payment processing
        booking.is_paid = True
        booking.save()
        messages.success(request, "Payment successful! Booking confirmed.")
        return redirect('user_bookings')
    return redirect('payment_page', booking_id=booking.id)

@staff_member_required
def admin_analytics(request):
    total_users = User.objects.count()
    total_providers = Profile.objects.filter(role='PROVIDER').count()
    total_services = Service.objects.count()
    total_bookings = Booking.objects.count()
    total_revenue = Booking.objects.filter(is_paid=True).aggregate(Sum('service__price'))['service__price__sum'] or 0
    
    context = {
        'total_users': total_users,
        'total_providers': total_providers,
        'total_services': total_services,
        'total_bookings': total_bookings,
        'total_revenue': total_revenue,
    }
    return render(request, 'admin_analytics.html', context)
