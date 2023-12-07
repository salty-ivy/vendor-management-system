from rest_framework.routers import DefaultRouter

from vendor.views import VendorViewSet

app_name = "vendor"

vendor_router = DefaultRouter()
vendor_router.register(r"", VendorViewSet, basename="vendor")
