from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from vouchers.models import Voucher
from .models import Claim


@login_required
def claim_voucher(request, voucher_id):

    voucher = get_object_or_404(Voucher, id=voucher_id)

    already = Claim.objects.filter(
        user=request.user,
        voucher=voucher
    ).exists()

    if not already:
        Claim.objects.create(
            user=request.user,
            voucher=voucher
        )

    return redirect("my_claims")


@login_required
def my_claims(request):

    claims = Claim.objects.filter(
        user=request.user
    )

    return render(request, "my_claims.html", {
        "claims": claims
    })