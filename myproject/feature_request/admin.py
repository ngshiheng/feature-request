from django.contrib import admin
from .models import Request


class RequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'priority', 'target_date', 'product_area')


admin.site.register(Request, RequestAdmin)
