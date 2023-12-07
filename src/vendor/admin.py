from django.contrib import admin

from vendor.models import Vendor

# Register your models here.


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    search_fields = ("name", "address", "vendor_code")
    list_display = (
        "name",
        "id",
        "contact_details",
        "address",
        "vendor_code",
    )
