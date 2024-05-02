from django.db import models
from vendor.models import Vendor

STATUS = (
    ('pending', 'Pending'),
    ('complete', 'Completed Successfully'),
    ('cancelled', 'Cancelled'),
)

class PurchaseOrder(models.Model):
    """
    Model to capture details of each purchase order and calculate various performance metrics.
    """
    po_number = models.CharField(max_length=255, unique=True, verbose_name="PO Number")
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name="Vendor")
    order_date = models.DateTimeField(verbose_name="Order Date")
    delivery_date = models.DateTimeField(verbose_name="Delivery Date")
    items = models.JSONField(verbose_name="Items Ordered")
    quantity = models.IntegerField(verbose_name="Total Quantity")
    status = models.CharField(max_length=255, choices=STATUS, verbose_name="Status")
    quality_rating = models.FloatField(null=True, blank=True, verbose_name="Quality Rating")
    issue_date = models.DateTimeField(verbose_name="Issue Date")
    acknowledgment_date = models.DateTimeField(null=True, blank=True, verbose_name="Acknowledgment Date")

    def __str__(self):
        return self.po_number

    class Meta:
        verbose_name = "Purchase Order"
        verbose_name_plural = "Purchase Orders"