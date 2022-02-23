from django.contrib import admin
from .models import User, Lead


# Register your models here.

# Create separate admin site for leads creation

# class SalesAdmin(admin.AdminSite):
#     site_header = 'Sales Admin'

class salesAdminPermission(admin.ModelAdmin):

    def has_add_permission(self, request, obj = None):
        if request.user.is_staff:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_staff:
            return True
        return False




# sales_admin = SalesAdmin(name="Sales_Admin")
#
# sales_admin.register(Lead)

admin.site.register(User)

admin.site.register(Lead,salesAdminPermission)

