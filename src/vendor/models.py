from uuid import uuid4

from django.db import models


class BaseMetrics(models.Model):
    """
    Abstract base class for common metrics shared among different models.
    """

    on_time_delivery_rate = models.FloatField(
        default=0, help_text="Percentage of on-time deliveries."
    )
    quality_rating_avg = models.FloatField(
        default=0, help_text="Average quality rating."
    )
    average_response_time = models.FloatField(
        default=0, help_text="Average response time in hours."
    )
    fulfillment_rate = models.FloatField(
        default=0, help_text="Percentage of fulfillment rate."
    )

    class Meta:
        abstract = True


class Vendor(BaseMetrics):
    """
    Model representing a vendor with specific metrics.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        db_index=True,
        unique=True,
        help_text="Unique identifier for the vendor.",
    )
    name = models.CharField(max_length=50, help_text="Name of the vendor.")
    contact_details = models.TextField(
        max_length=150, help_text="Contact details of the vendor."
    )
    address = models.TextField(max_length=200, help_text="Address of the vendor.")
    vendor_code = models.CharField(
        max_length=10,
        unique=True,
        db_index=True,
        help_text="Unique code assigned to the vendor.",
    )

    def __str__(self):
        """
        String representation of the Vendor object.

        Returns:
        str: Name of the vendor.
        """
        return self.name
