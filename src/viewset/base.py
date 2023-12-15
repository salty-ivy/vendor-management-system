from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from exceptions.base import HttpException


class BaseAutoViewset(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    A base viewset that provides `retrieve`, `create`, `list`, `update`, `delete` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

    # overriding create method to return custom http exception

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        operation = self.perform_create(serializer)
        if isinstance(operation, Exception):
            exception = HttpException(detail=operation)
            return exception.error_response()
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    # overriding perform_create to raise E if save is failed

    def perform_create(self, serializer):
        try:
            serializer.save()
        except Exception as E:
            return E
