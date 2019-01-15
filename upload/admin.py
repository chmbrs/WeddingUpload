from django.contrib import admin

from .models import Photo

# Register your models here.
@admin.register(Photo)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("upload", "uploaded_at", "get_num_of_likes", 'slug', "publish" )
    list_editable = ["publish"]
