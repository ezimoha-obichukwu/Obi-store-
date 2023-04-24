from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('about/', views.about_page, name="about"),
    path('contact/', views.contact_page, name="contact"),
    path('product/', views.product_page, name="product"),
    path('single-product-page/', views.single_product_page, name="single-product-page")

]