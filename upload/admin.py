from django.contrib import admin
from django.db.models import Count
from .models import Photo

# Register your models here.
@admin.register(Photo)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("upload", "uploaded_at","liked_by", "num_of_likes", "publish" )
    list_editable = ["publish"]
