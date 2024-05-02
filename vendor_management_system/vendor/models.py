from django.db import models

class Vendor(models.Model):
    """
    Model to store essential information about each vendor and their performance metrics.
    """
    name = models.CharField(max_length=255, help_text="Vendor's name.")
    contact_details = models.TextField(help_text="Contact information of the vendor.")
    address = models.TextField(help_text="Physical address of the vendor.")
    vendor_code = models.CharField(max_length=50, unique=True, help_text="A unique identifier for the vendor.")
    on_time_delivery_rate = models.FloatField(help_text="Tracks the percentage of on-time deliveries.")
    quality_rating_avg = models.FloatField(help_text="Average rating of quality based on purchase orders.")
    average_response_time = models.FloatField(help_text="Average time taken to acknowledge purchase orders.")
    fulfillment_rate = models.FloatField(help_text="Percentage of purchase orders fulfilled successfully.")

    def __str__(self):
        return self.name

