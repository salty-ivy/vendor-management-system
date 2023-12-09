from rest_framework import mixins, viewsets


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

    pass
