from django.contrib import admin
from .models import product,Reviews
from import_export.admin import ImportExportModelAdmin

class productAdminview(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['name','price','image']
    search_fields=['name']
    list_filter=['name']
    list_per_page = 10

class ReviewsAdminview(ImportExportModelAdmin):
    list_display=['product_review','name','email']

# Register your models here.
admin.site.register(product,productAdminview)
admin.site.register(Reviews,ReviewsAdminview)