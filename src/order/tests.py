from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from order.models import PurchaseOrder
from vendor.models import Vendor


class PurchaseOrderTests(APITestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="testvendor",
            contact_details="testcontactdetails",
            address="testaddress",
            vendor_code="testcode",
        )
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)
        self.purchase_order = PurchaseOrder.objects.create(
            po_number="1234567890",
            vendor=self.vendor,
            order_date="2021-01-01",
            delivery_date="2021-01-02",
            status="completed",
            quality_rating=5,
            acknowledgment_date="2021-01-01",
        )

    def test_create_purchase_order(self):
        """
        Ensure we can create a new purchase order object.
        """
        url = reverse("order:order-list")
        data = {
            "po_number": "75613",
            "vendor": self.vendor.vendor_code,
            "order_date": "2023-12-07T10:07:25Z",
            "delivery_date": "2023-12-11T18:00:00Z",
            "items": {"bag": "red", "bottle": "blue"},
            "quantity": 23,
            "status": "pending",
            "quality_rating": 3.0,
            "issue_date": "2023-12-07T10:08:51.649033Z",
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(), 2)
        self.assertIn(
            PurchaseOrder.objects.filter(vendor=self.vendor).last().po_number,
            "75613",
        )

    def test_get_purchase_order(self):
        """
        Ensure we can get a purchase order object.
        """
        url = reverse("order:order-detail", args=[self.purchase_order.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["po_number"], "1234567890")

    def test_update_purchase_order(self):
        """
        Ensure we can update a purchase order object.
        """
        url = reverse("order:order-detail", args=[self.purchase_order.id])
        data = {
            "po_number": "75613",
            "vendor": self.vendor.vendor_code,
            "order_date": "2021-01-01",
            "delivery_date": "2021-01-02",
            "items": {"bag": "red", "bottle": "blue", "book": "green"},
            "quantity": 50,
            "status": "completed",
            "quality_rating": 5,
            "acknowledgment_date": "2021-01-01",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            PurchaseOrder.objects.get(vendor=self.vendor).po_number, "75613"
        )

    def test_delete_purchase_order(self):
        """
        Ensure we can delete a purchase order object.
        """
        url = reverse("order:order-detail", args=[self.purchase_order.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PurchaseOrder.objects.count(), 0)
