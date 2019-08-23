from django.contrib import admin

# Register your models here.
from .models import FEP, ACTION, EQUIPMENT

admin.site.register(FEP)
admin.site.register(ACTION)
admin.site.register(EQUIPMENT)
