from rest_framework.routers import DefaultRouter

from order.views import PurchaseOrderViewset

app_name = "order"

router = DefaultRouter()
router.register(r"", PurchaseOrderViewset, basename="order")


urlpatterns = router.urls
