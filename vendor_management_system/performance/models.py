from django.db import models
from vendor.models import Vendor

class Performance(models.Model):
    """
    This model optionally stores historical data on vendor performance, enabling trend analysis.
    """

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, help_text="Link to the Vendor model.")
    date = models.DateTimeField(help_text="Date of the performance record.")
    on_time_delivery_rate = models.FloatField(help_text="Historical record of the on-time delivery rate.")
    quality_rating_avg = models.FloatField(help_text="Historical record of the quality rating average.")
    average_response_time = models.FloatField(help_text="Historical record of the average response time.")
    fulfillment_rate = models.FloatField(help_text="Historical record of the fulfilment rate.")

    def __str__(self):
        return f"{self.vendor} - {self.date}"
