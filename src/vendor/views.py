from rest_framework import viewsets

from vendor.models import Vendor


class VendorViewSet(viewsets.ViewSet):
    """
    A viewset for viewing and editing vendor instances.
    """

    queryset = Vendor.objects.all()
