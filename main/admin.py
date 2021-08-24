from django.contrib import admin

from django.contrib.admin import ModelAdmin

from main.models import *


class CarsImageInLine(admin.TabularInline):
    model = CarsImage
    max_num = 10
    min_num = 1


@admin.register(Cars)
class PostAdmin(admin.ModelAdmin):
    inlines = [CarsImageInLine]


admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(CarsImage)