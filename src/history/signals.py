from django.db.models.signals import post_save
from django.dispatch import receiver

from history.utils import historical_performance_handler, revaluation_perofmance
from order.models import PurchaseOrder


@receiver(post_save, sender=PurchaseOrder)
def create_historical_performace_hook(sender, instance, created, **kwargs):
    """
    Signal handler to create a HistoricalPerformance instance when a PurchaseOrder is saved.
    """

    if created:
        historical_performance_handler(instance)
    else:
        revaluation_perofmance(instance)
