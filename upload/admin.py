from django.contrib import admin

from .models import Photos

# Register your models here.
@admin.register(Photos)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("upload", "uploaded_at", "publish" )
    list_editable = ["publish"]
