from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(f'<img src = "{object.car_photo.url}" width="40" />')
    thumbnail.short_description = 'Car Image'
    list_display = ('id','car_title','thumbnail','city','color','model','year', 'price', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id','thumbnail', 'car_title',)
    list_editable = ('is_featured',)
    search_fields = ('id','city','car_title', 'model', 'price', 'is_featured')
    list_filter = ('city', 'model', 'body_style','fuel_type')
admin.site.register(Car, CarAdmin)