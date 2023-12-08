from django.db.models import Avg, F

from history.models import HistoricalPerformance
from order.models import PurchaseOrder


def calculate_delivery_and_fullfilment_rate(vendor):
    completed_po_count = PurchaseOrder.objects.filter(
        vendor=vendor,
        status="completed",
    ).count()
    all_po_count = PurchaseOrder.objects.filter(vendor=vendor).count()

    on_time_delivery_rate = (
        0 if completed_po_count == 0 else completed_po_count / all_po_count
    )

    fulfilment_rate = 0 if all_po_count == 0 else completed_po_count / all_po_count

    return on_time_delivery_rate, fulfilment_rate


def calculate_on_quality_rating_avg(vendor):
    return PurchaseOrder.objects.filter(
        vendor=vendor, quality_rating__isnull=False
    ).aggregate(quality_rating_avg=Avg("quality_rating"))["quality_rating_avg"]


def calculate_avg_response_time(vendor):
    avg_response_time_delta = PurchaseOrder.objects.filter(
        vendor=vendor, acknowledgment_date__isnull=False
    ).aggregate(avg_response_time=Avg(F("acknowledgment_date") - F("issue_date")))[
        "avg_response_time"
    ]
    avg_response_time_seconds = avg_response_time_delta.total_seconds()
    avg_response_time_hours = avg_response_time_seconds / 3600.0

    return avg_response_time_hours


def historical_performance_handler(instance):
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

    on_time_delivery_rate, fulfilment_rate = calculate_delivery_and_fullfilment_rate(
        vendor
    )

    quality_rating_avg = calculate_on_quality_rating_avg(vendor)

    if instance.acknowledgment_date is not None:
        avg_response_time_hours = calculate_avg_response_time(vendor)
    else:
        avg_response_time_hours = 0.0

    hp = HistoricalPerformance.objects.create(
        vendor=vendor,
        on_time_delivery_rate=on_time_delivery_rate,
        quality_rating_avg=quality_rating_avg,
        average_response_time=avg_response_time_hours,
        fulfillment_rate=fulfilment_rate,
    )
    hp.save()

    # updating vendor metrics Field
    vendor.on_time_delivery_rate = on_time_delivery_rate
    vendor.quality_rating_avg = quality_rating_avg
    vendor.average_response_time = avg_response_time_hours
    vendor.fulfilment_rate = fulfilment_rate
    vendor.save()


def revaluation_perofmance(instance):
    vendor = instance.vendor
    history_instance = (
        HistoricalPerformance.objects.filter(vendor=vendor).order_by("date").last()
    )

    if instance.acknowledgment_date is not None:
        avg_response_time_hours = calculate_avg_response_time(vendor)
    else:
        avg_response_time_hours = 0.0

    history_instance.average_response_time = avg_response_time_hours
    history_instance.save()

    vendor.average_response_time = avg_response_time_hours
    vendor.save()
