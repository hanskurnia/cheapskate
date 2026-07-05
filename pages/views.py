from django.shortcuts import render
from vouchers.models import Voucher

def home(request):
    vouchers = Voucher.objects.filter(is_active=True)

    context = {
        'vouchers': vouchers
    }

    return render(request, 'home.html', context)