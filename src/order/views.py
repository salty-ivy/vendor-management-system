from django.utils.timezone import now
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from order.models import PurchaseOrder
from order.serializers import (
    PurchaseOrderCreateUpdateSerializer,
    PurchaseOrderRetrieveListSerializer,
)
from viewset.base import BaseAutoViewset


class PurchaseOrderViewset(BaseAutoViewset):
    """
    A viewset for viewing and editing vendor instances.
    """

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderRetrieveListSerializer
    create_update_serializer_class = PurchaseOrderCreateUpdateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.create_update_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.create_update_serializer_class(
            instance, data=request.data, partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def acknowledge(self, request, pk=None):
        po = PurchaseOrder.objects.get(id=pk)
        if po.acknowledgment_date is None:
            po.acknowledgment_date = now()
            po.save()

            return Response(
                {
                    "detail": f"Purchase order {po.po_number} has been acknowledged successfully",
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {
                "detail": f"Purchase order {po.po_number} has already been acknowledged",
            },
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
