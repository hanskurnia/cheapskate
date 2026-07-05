from django.db import models
from categories.models import Category

class Voucher(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    discount = models.IntegerField()
    expired_date = models.DateField()
    image = models.ImageField(upload_to='vouchers/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title