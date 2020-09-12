from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='product_home'),
    path('about/', views.about_view, name='product_about'),
    path('contact/', views.contact_view, name='product_contact'),
    path('create_product/', views.create_product, name='product_create'),
    path('edit_product/<int:pk>/', views.edit_product, name='product_edit'),
    path('delete_product/<int:pk>/', views.delete_product, name='product_delete'),
    path('categories/', views.categories_view, name='categories_home'),
    path('create_category', views.create_category, name='category_create'),
    path('categories/edit_category/<int:pk>/', views.edit_category, name='category_edit'),
    path('categories/delete_category/<int:pk>/', views.delete_category, name='category_delete'),    
]