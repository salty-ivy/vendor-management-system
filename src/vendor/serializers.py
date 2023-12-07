from rest_framework import serializers

from .models import Vendor


class VendorSerializer(serializers.Serializer):
    """
    Serializer for Vendor model
    """

    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=50)
    contact_details = serializers.CharField(max_length=150)
    address = serializers.CharField(max_length=200)
    vendor_code = serializers.CharField(max_length=10)

    on_time_delivery_rate = serializers.FloatField(default=0)
    quality_rating_avg = serializers.FloatField(default=0)
    average_response_time = serializers.FloatField(default=0)
    fulfillment_rate = serializers.FloatField(default=0)

    def create(self, validated_data):
        return Vendor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.contact_details = validated_data.get(
            "contact_details", instance.contact_details
        )
        instance.address = validated_data.get("address", instance.address)
        instance.vendor_code = validated_data.get("vendor_code", instance.vendor_code)

        instance.on_time_delivery_rate = validated_data.get(
            "on_time_delivery_rate", instance.on_time_delivery_rate
        )
        instance.quality_rating_avg = validated_data.get(
            "quality_rating_avg", instance.quality_rating_avg
        )
        instance.average_response_time = validated_data.get(
            "average_response_time", instance.average_response_time
        )
        instance.fulfillment_rate = validated_data.get(
            "fulfillment_rate", instance.fulfillment_rate
        )

        instance.save()
        return instance
