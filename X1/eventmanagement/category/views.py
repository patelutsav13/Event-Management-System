from django.shortcuts import render

# Create your views here.

from .models import Categories

def view_event(request):
    categories = Categories.objects.all().order_by('categoryname')  # ✅ correct field
    return render(request , 'view_events.html', {'categories': categories})
