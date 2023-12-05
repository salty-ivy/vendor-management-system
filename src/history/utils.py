from django.db.models import Avg, F

from history.models import HistoricalPerformance
from order.models import PurchaseOrder


def historical_performance_handler(sender, instance, **kwargs):
    """
    Update historical performance metrics based on changes in the PurchaseOrder model.

    Args:
    sender: The sender of the signal.
    instance (PurchaseOrder): The instance of the PurchaseOrder model that triggered the signal.
    kwargs: Additional keyword arguments.

    Returns:
    None
    """

    vendor = instance.vendor
    completed_po_count = PurchaseOrder.objects.filter(
        vendor=vendor, status="completed"
    ).count()
    all_po_count = PurchaseOrder.objects.filter(vendor=vendor).count()

    on_time_delivery_rate = (
        0 if completed_po_count == 0 else completed_po_count / all_po_count
    )

    quality_rating_avg = PurchaseOrder.objects.filter(
        vendor=vendor, quality_rating__isnull=False
    ).aggregate(Avg("quality_rating"))["quality_rating__avg"]

    avg_response_time = PurchaseOrder.objects.filter(
        vendor=vendor, acknowledgment_date__isnull=False
    ).aggregate(Avg(F("delivery_date") - F("acknowledgment_date")))[
        "delivery_date__avg"
    ]

    fulfilment_rate = 0 if all_po_count == 0 else completed_po_count / all_po_count

    hp = HistoricalPerformance.objects.create(
        vendor=vendor,
        on_time_delivery_rate=on_time_delivery_rate,
        quality_rating_avg=quality_rating_avg,
        average_response_time=avg_response_time,
        fulfillment_rate=fulfilment_rate,
    )
    hp.save()
