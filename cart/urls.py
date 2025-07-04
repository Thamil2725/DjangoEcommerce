from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('add/<int:product_id>/', views.add_to_cart, name='cart_add'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='cart_remove'),
    path('update/<int:product_id>/', views.update_cart_quantity, name='cart_update'),
]
