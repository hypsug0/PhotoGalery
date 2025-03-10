from django.contrib import admin

from .models import Photo, Tags

# Register your models here.


admin.site.register(Tags, admin.ModelAdmin)
admin.site.register(Photo, admin.ModelAdmin)
