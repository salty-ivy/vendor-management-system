from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from history.models import HistoricalPerformance
from vendor.models import Vendor


class VendorTests(APITestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="testvendor",
            contact_details="testcontactdetails",
            address="testaddress",
            vendor_code="testvendorcode",
        )
        self.historical_performance = HistoricalPerformance.objects.create(
            vendor=self.vendor,
            on_time_delivery_rate=0.5,
            quality_rating_avg=3.5,
            average_response_time=2.5,
            fulfillment_rate=0.5,
        )

        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)

    def test_get_vendor(self):
        """
        Ensure we can get a vendor object.
        """
        url = reverse("vendor:vendor-detail", args=[self.vendor.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "testvendor")

    def test_get_historical_performance(self):
        """
        Ensure we can get a historical performance object.
        """
        url = reverse(
            "vendor:vendor-performance", args=[self.historical_performance.id]
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["metrics"]["vendor"], self.vendor.id)
