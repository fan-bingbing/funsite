from django.contrib import admin

# Register your models here.
from .models import FEP, ACTION

admin.site.register(FEP)
admin.site.register(ACTION)
