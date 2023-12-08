from uuid import uuid4

from django.db import models

from vendor.models import BaseMetrics, Vendor


class HistoricalPerformance(BaseMetrics):
    """
    Model representing the historical performance metrics of a vendor.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        db_index=True,
        unique=True,
        help_text="Unique identifier for the HistoricalPerformance.",
    )
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        help_text="Vendor associated with the historical performance.",
    )
    date = models.DateTimeField(
        auto_now_add=True,
        help_text="Date when the historical performance was recorded.",
    )

    def __str__(self):
        """
        String representation of the HistoricalPerformance object.

        Returns:
        str: Name of the associated vendor.
        """
        return f"History--{self.vendor.name}--{self.id}"
