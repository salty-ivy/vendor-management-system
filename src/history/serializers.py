from rest_framework import serializers

from vendor.serializers import VendorSerializer


class HistoricalPerformanceSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    vendor = VendorSerializer(read_only=True)
    on_time_delivery_rate = serializers.FloatField(default=0)
    quality_rating_avg = serializers.FloatField(default=0)
    average_response_time = serializers.FloatField(default=0)
    fulfillment_rate = serializers.FloatField(default=0)
    date = serializers.DateTimeField(read_only=True)
