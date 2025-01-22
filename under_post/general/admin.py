from .models import *
from django.contrib import admin


class OrderAdmin(admin.ModelAdmin):
    list_display = ['index', 'full_name', 'phone', 'email']
    search_fields = ['phone', 'email', 'index']


admin.site.register(Order, OrderAdmin)
