from django.contrib import admin

# Register your models here.

from .models import employees,company

admin.site.register(employees)
admin.site.register(company)
