from django.contrib import admin

from .models import Socials, User

# Register your models here.


admin.site.register(User, admin.ModelAdmin)
admin.site.register(Socials, admin.ModelAdmin)
