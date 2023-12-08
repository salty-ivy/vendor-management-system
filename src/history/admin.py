from django.contrib import admin

from history.models import HistoricalPerformance

# Register your models here.


@admin.register(HistoricalPerformance)
class HistoficalPerformanceAdmin(admin.ModelAdmin):
    search_fields = ("vendor",)
    list_display = (
        "id",
        "on_time_delivery_rate",
        "quality_rating_avg",
        "average_response_time",
        "fulfillment_rate",
    )
