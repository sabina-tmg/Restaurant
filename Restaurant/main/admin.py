from django.contrib import admin
from .models import Momo,Touch,Menu
#register your models here.
admin.site.register(Touch)
@admin.register(Momo)
class MomoAdmin(admin.ModelAdmin):
    list_display=['id','category','price','title','image']

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=['id','category','price','title','image']
