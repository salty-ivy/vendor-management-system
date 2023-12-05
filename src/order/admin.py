from django.contrib import admin

from order.models import PurchaseOrder

# Register your models here.


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    search_fields = ("po_number", "status", "vendor")
    list_display = (
        "po_number",
        "vendor",
        "order_date",
        "delivery_date",
        "acknowledgment_date",
        "issue_date",
        "status",
    )
