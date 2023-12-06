from rest_framework.routers import DefaultRouter

from vendor.views import VendorViewSet

app_name = "vendor"

router = DefaultRouter()
router.register(r"", VendorViewSet, basename="vendor")

urlpatterns = router.urls
