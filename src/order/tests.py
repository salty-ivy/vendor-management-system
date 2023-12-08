from django.test import TestCase

# from rest_framework import status
from rest_framework.test import APIClient

# from django.utils.timezone import now
from order.models import PurchaseOrder

# from order.serializers import PurchaseOrderRetrieveListSerializer, PurchaseOrderCreateUpdateSerializer


class PurchaseOrderViewsetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.purchase_order_data = {
            # Provide necessary data for creating a PurchaseOrder
            # Adjust the data based on your serializer requirements
        }
        self.purchase_order = PurchaseOrder.objects.create(**self.purchase_order_data)
