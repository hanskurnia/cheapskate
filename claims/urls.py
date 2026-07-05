from django.urls import path
from . import views

urlpatterns = [
    path("claim/<int:voucher_id>/", views.claim_voucher, name="claim_voucher"),
    path("my-claims/", views.my_claims, name="my_claims"),
]