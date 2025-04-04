from django.contrib import admin

from .models import Album, Photo, Tags


# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("label",)}


class PhotoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("album", "name")}


admin.site.register(Album, AlbumAdmin)
admin.site.register(Tags, admin.ModelAdmin)
admin.site.register(Photo, PhotoAdmin)
