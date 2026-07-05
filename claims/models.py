from django.db import models
from django.contrib.auth.models import User
from vouchers.models import Voucher

class Claim(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    claim_date = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)