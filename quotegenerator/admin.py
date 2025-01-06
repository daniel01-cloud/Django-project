from django.contrib import admin
from .models import Quotes
from django.utils.safestring import mark_safe  # Importing mark_safe

class QuotesAdmin(admin.ModelAdmin):
    list_display = ('quote_text', 'author_name', 'image_preview')

    def image_preview(self, obj):
        return mark_safe(f'<img src="{obj.image_url}" style="width: 100px; height: auto;" />')

    image_preview.short_description = 'Image'

admin.site.register(Quotes, QuotesAdmin)
