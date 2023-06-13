from django.contrib import admin
from.models import Category,SubCategory
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CategoryAdminview(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['category_name','Category_image','status']

admin.site.register(Category,CategoryAdminview)
admin.site.register(SubCategory)