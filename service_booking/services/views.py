from django.shortcuts import render
from .models import Service, Category

def home(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()
    
    if category_id:
        services = Service.objects.filter(category_id=category_id)
    else:
        services = Service.objects.all()
        
    return render(request, 'home.html', {
        'services': services,
        'categories': categories,
        'active_category': int(category_id) if category_id else None
    })