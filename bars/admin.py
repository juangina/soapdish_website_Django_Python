from django.contrib import admin

from .models import Bar

class BarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'recipe','nutrients','exfolients','clays', 'price', 'batch_code','is_cured', 'for_sale')
    list_display_links = ('id', 'name')
    list_editable = ('nutrients','exfolients', 'clays', 'is_cured','for_sale')
    search_fields = ('name',)
    list_per_page = 50


admin.site.register(Bar, BarsAdmin)
