from rest_framework import status
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from history.models import HistoricalPerformance
from history.serializers import HistoricalPerformanceSerializer
from vendor.models import Vendor
from vendor.serializers import VendorSerializer
from viewset.base import BaseAutoViewset


class VendorViewSet(BaseAutoViewset):
    """
    A viewset for viewing and editing vendor instances.
    """

    permission_classes = (IsAuthenticated,)
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]

    queryset = Vendor.objects.all()

    serializer_class = VendorSerializer
    history_serializer = HistoricalPerformanceSerializer

    @action(detail=True, methods=["get"])
    def performance(self, request, pk=None):
        history_queryset = HistoricalPerformance.objects.filter(
            vendor=pk
        ).prefetch_related("vendor")

        # get the vendor from the first element
        vendor = history_queryset.first().vendor

        serializer = self.history_serializer(history_queryset, many=True)
        headers = self.get_success_headers(serializer.data)

        content = {
            "on_time_delivery_rate": vendor.on_time_delivery_rate,
            "quality_rating_avg": vendor.quality_rating_avg,
            "average_response_time": vendor.average_response_time,
            "fulfillment_rate": vendor.fulfillment_rate,
            "performance_history": serializer.data,
        }

        return Response(content, status=status.HTTP_201_CREATED, headers=headers)
