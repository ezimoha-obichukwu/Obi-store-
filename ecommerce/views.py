from django.shortcuts import render
from .models import Category

# Create your views here.
def home_page(request):
    all_categories = Category.objects.all()
    context = {
        "all_categories": all_categories
    }
    return render(request, "index.html", context)

def about_page(request):
    return render(request, "about.html")

def contact_page(request):
    return render(request, "contact.html")

def product_page(request):
    return render(request, "products.html")

def single_product_page(request):
    return render(request, "single-product.html")