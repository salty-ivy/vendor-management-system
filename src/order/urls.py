from rest_framework.routers import DefaultRouter

from order.views import PurchaseOrderViewset

app_name = "order"

order_router = DefaultRouter()
order_router.register(r"", PurchaseOrderViewset, basename="order")
