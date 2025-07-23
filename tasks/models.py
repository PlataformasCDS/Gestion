from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils import timezone

class SocialReason(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    social_reason = models.ForeignKey('tasks.SocialReason', on_delete=models.SET_NULL, null=True, blank=True)

"""
class PurchaseOrder(models.Model):
    social_reason = models.ForeignKey(SocialReason, on_delete=models.CASCADE)
    correlativo = models.PositiveIntegerField()
    year = models.PositiveIntegerField(default=timezone.now().year)
    provider_name = models.CharField(max_length=255)
    provider_rut = models.CharField(max_length=20)
    provider_address = models.CharField(max_length=255)
    provider_city = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    requested_by = models.CharField(max_length=100)
    attention = models.CharField(max_length=100)
    invoice_type = models.CharField(
        max_length=20,
        choices=[
            ("factura", "Factura (19%)"),
            ("boleta", "Boleta Honorarios (14.5%)")
        ],
        default="factura"
    )
    currency = models.CharField(max_length=20, default="CLP")
    bill_to = models.CharField(max_length=255)
    internal_use = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    quote_file = models.FileField(upload_to="quotes/", null=True, blank=True)
    approved_by = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="approved_orders")
    returned = models.BooleanField(default=False)

    class Meta:
        unique_together = ('social_reason', 'correlativo', 'year')

    def __str__(self):
        return f"{str(self.correlativo).zfill(3)}/{self.year}"

    def total(self):
        subtotal = sum([item.total_value() for item in self.items.all()])
        if self.invoice_type == "factura":
            return subtotal * 1.19
        else:
            return subtotal * 1.145

    def subtotal(self):
        return sum([item.total_value() for item in self.items.all()])

    def tax(self):
        subtotal = self.subtotal()
        return subtotal * 0.19 if self.invoice_type == "factura" else subtotal * 0.145


class PurchaseOrderItem(models.Model):
    order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name="items")
    quantity = models.PositiveIntegerField()
    code = models.CharField(max_length=100)
    description = models.TextField()
    unit_value = models.DecimalField(max_digits=12, decimal_places=2)

    def total_value(self):
        return self.quantity * self.unit_value

    def __str__(self):
        return self.description
"""