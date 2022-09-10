from django.contrib import admin

from .models import Admin, Client, Order, Status

# Register your models here.
admin.site.register(Client)
admin.site.register(Admin)
admin.site.register(Status)
admin.site.register(Order)
