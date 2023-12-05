from uuid import uuid4

from django.db import models
from django.utils.timezone import now

from order.constants import STATUS

# Create your models here.
from vendor.models import Vendor


class PurchaseOrder(models.Model):
    """
    Model representing a purchase order with details.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        db_index=True,
        unique=True,
        help_text="Unique identifier for the purchase_order.",
    )
    po_number = models.CharField(max_length=10, help_text="Purchase order number.")
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        help_text="Vendor associated with the purchase order.",
    )
    order_date = models.DateTimeField(
        default=now, help_text="Date when the purchase order was created."
    )
    delivery_date = models.DateTimeField(help_text="Expected delivery date.")
    items = models.JSONField(
        default=dict, help_text="JSON representation of ordered items."
    )
    quantity = models.PositiveIntegerField(
        default=0, help_text="Total quantity of items in the order."
    )
    status = models.CharField(
        choices=STATUS, max_length=100, help_text="Status of the purchase order."
    )
    quality_rating = models.FloatField(
        null=True, blank=True, help_text="Quality rating for the purchase."
    )
    issue_date = models.DateTimeField(
        auto_now_add=True, help_text="Date when the purchase order was issued."
    )
    acknowledgment_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Date when the purchase order was acknowledged.",
    )

    def __str__(self):
        """
        String representation of the PurchaseOrder object.

        Returns:
        str: Purchase order number.
        """
        return self.po_number
