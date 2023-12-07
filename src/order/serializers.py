# serializers.py
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from order.constants import STATUS
from vendor.models import Vendor
from vendor.serializers import VendorSerializer

from .models import PurchaseOrder


class PurchaseOrderCreateUpdateSerializer(serializers.Serializer):
    """
    Serializer for PurchaseOrder model, dealing with creation and updation
    """

    id = serializers.UUIDField(read_only=True)
    po_number = serializers.CharField(max_length=10)
    vendor = serializers.CharField(
        max_length=10
    )  # Use write_only to exclude from response
    order_date = serializers.DateTimeField()
    delivery_date = serializers.DateTimeField()
    items = serializers.JSONField()
    quantity = serializers.IntegerField()
    status = serializers.ChoiceField(choices=STATUS)
    quality_rating = serializers.FloatField(allow_null=True, required=False)
    acknowledgment_date = serializers.DateTimeField(allow_null=True, required=False)

    def create(self, validated_data):
        vendor_code = validated_data.pop("vendor")

        # Create or update the associated vendor
        vendor_instance = get_object_or_404(Vendor, vendor_code=vendor_code)
        # Create a new PurchaseOrder instance and associate it with the vendor
        return PurchaseOrder.objects.create(vendor=vendor_instance, **validated_data)

    def update(self, instance, validated_data):
        # Update the PurchaseOrder fields
        instance.po_number = validated_data.get("po_number", instance.po_number)
        instance.order_date = validated_data.get("order_date", instance.order_date)
        instance.delivery_date = validated_data.get(
            "delivery_date", instance.delivery_date
        )
        instance.items = validated_data.get("items", instance.items)
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.status = validated_data.get("status", instance.status)
        instance.quality_rating = validated_data.get(
            "quality_rating", instance.quality_rating
        )
        instance.acknowledgment_date = validated_data.get(
            "acknowledgment_date", instance.acknowledgment_date
        )

        # Extract and update vendor data
        vendor_code = validated_data.pop("vendor")
        vendor_instance = get_object_or_404(Vendor, vendor_code=vendor_code)

        # Associate the updated vendor with the PurchaseOrder
        instance.vendor = vendor_instance

        instance.save()
        return instance


class PurchaseOrderRetrieveListSerializer(serializers.Serializer):
    """
    Serializer dealing with retrieval and indexed listing of PurchaseOrder instances
    """

    id = serializers.UUIDField(read_only=True)
    po_number = serializers.CharField(max_length=10)
    vendor = VendorSerializer(
        read_only=True
    )  # Use read_only to exclude from create/update
    order_date = serializers.DateTimeField()
    delivery_date = serializers.DateTimeField()
    items = serializers.JSONField()
    quantity = serializers.IntegerField()
    status = serializers.ChoiceField(choices=STATUS)
    quality_rating = serializers.FloatField(allow_null=True, required=False)
    issue_date = serializers.DateTimeField(read_only=True)
    acknowledgment_date = serializers.DateTimeField(allow_null=True, required=False)
