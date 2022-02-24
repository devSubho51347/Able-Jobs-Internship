from django.contrib import admin
from .models import User, Lead

# for import/export integration
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.

# Create separate admin site for leads creation

class SalesAdmin(admin.AdminSite):
    site_header = 'Sales Admin'


## class for creating import/export
class LeadImportExport(resources.ModelResource):
    class Meta:
        model = Lead
        skip_unchanged = True
        report_skipped = False


# Admin integration of the import export feature and providing access permissions to user_specific
class LeadImportAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = LeadImportExport

    def has_add_permission(self, request, obj=None):
        if request.user.is_staff:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_staff:
            return True
        return False


# class salesAdminPermission(admin.ModelAdmin):
#
#     def has_add_permission(self, request, obj=None):
#         if request.user.is_staff:
#             return True
#         return False
#
#     def has_delete_permission(self, request, obj=None):
#         if request.user.is_staff:
#             return True
#         return False


sales_admin = SalesAdmin(name="Sales_Admin")
sales_admin.register(Lead, LeadImportAdmin)
#
# sales_admin.register(Lead)

admin.site.register(User)

admin.site.register(Lead, LeadImportAdmin)
