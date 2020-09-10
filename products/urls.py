from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='product_home'),
    path('about/', views.about_view, name='product_about'),
    path('contact/', views.contact_view, name='product_contact'),
    path('create_product/', views.create_product, name='product_create'),
    path('edit_product/<int:pk>/', views.edit_product, name='product_edit'),
    path('delete_product/<int:pk>/', views.delete_product, name='product_delete'),
]