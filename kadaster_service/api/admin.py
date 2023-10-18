from django.contrib import admin
from .models import RequestHistory

@admin.register(RequestHistory)
class RequestHistoryAdmin(admin.ModelAdmin):
    list_display = ("cadastre_number", "response", "timestamp")

