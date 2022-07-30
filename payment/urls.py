from django.urls import path
from . import views

urlpatterns = [
    path('contribute/', views.create_order, name='create order'),
    path('contribute/pay_handle/', views.payment_handler, name='payment handle')
]
