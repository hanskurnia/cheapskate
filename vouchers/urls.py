from django.urls import path
from . import views

urlpatterns = [
    path('', views.voucher_list, name='voucher_list'),
    path('<int:id>/', views.voucher_detail, name='voucher_detail'),
]