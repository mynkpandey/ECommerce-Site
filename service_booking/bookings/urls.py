from django.urls import path
from .views import book_service, provider_dashboard, update_booking_status, user_bookings, payment_page, process_payment, admin_analytics

urlpatterns = [
    path('book/<int:service_id>/', book_service, name='book_service'),
    path('provider-dashboard/', provider_dashboard, name='provider_dashboard'),
    path('update-booking/<int:booking_id>/<str:status>/', update_booking_status, name='update_booking'),
    path('my-bookings/', user_bookings, name='user_bookings'),
    path('payment/<int:booking_id>/', payment_page, name='payment_page'),
    path('process-payment/<int:booking_id>/', process_payment, name='process_payment'),
    path('admin-analytics/', admin_analytics, name='admin_analytics'),
]
