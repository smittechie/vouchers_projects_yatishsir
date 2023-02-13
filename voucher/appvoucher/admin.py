from django.contrib import admin

from .models import Employee, Company, Voucher

# Register your models here.
admin.site.register(Company),
admin.site.register(Voucher),
admin.site.register(Employee),