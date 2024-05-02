from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Activity



# Unregister and register again

admin.site.register(Activity)
