from django.shortcuts import render, get_object_or_404
from .models import Voucher
from categories.models import Category


def voucher_list(request):

    vouchers = Voucher.objects.filter(is_active=True)
    categories = Category.objects.all()

    search = request.GET.get("search")

    if search:
        vouchers = vouchers.filter(title__icontains=search)

    category = request.GET.get("category")

    if category:
        vouchers = vouchers.filter(category_id=category)

    return render(request, "voucher_list.html", {
        "vouchers": vouchers,
        "categories": categories,
    })


def voucher_detail(request, id):

    voucher = get_object_or_404(Voucher, id=id)

    return render(request, "voucher_detail.html", {
        "voucher": voucher
    })