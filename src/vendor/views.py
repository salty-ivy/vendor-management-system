from vendor.models import Vendor
from vendor.serializers import VendorSerializer
from viewset.base import BaseAutoViewset


class VendorViewSet(BaseAutoViewset):
    """
    A viewset for viewing and editing vendor instances.
    """

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
