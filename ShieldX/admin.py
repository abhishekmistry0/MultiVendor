from django.contrib import admin
from .models import UserProfile,UserRelatives,CarRegistration
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(UserProfile,ImportExportModelAdmin)
admin.site.register(UserRelatives,ImportExportModelAdmin)
admin.site.register(CarRegistration,ImportExportModelAdmin)