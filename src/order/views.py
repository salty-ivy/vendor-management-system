from rest_framework import viewsets

from order.models import PurchaseOrder


class PurchaseOrderViewset(viewsets.ViewSet):
    """
    A viewset for viewing and editing vendor instances.
    """

    queryset = PurchaseOrder.objects.all()
