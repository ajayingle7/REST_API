from django.contrib import admin
from .models import  Order
# Register your models here.


class orderAdmin(admin.ModelAdmin):
    list_display = ["oid","oname","status","mfg"]

admin.site.register(Order,orderAdmin)