from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='product_home'),
    path('about/', views.about_view, name='product_about'),
    path('contact/', views.contact_view, name='product_contact'),
]