from django.contrib             import admin

from import_export              import resources
from import_export.admin        import ImportExportModelAdmin

# Register your models here.

# admin.site.register(Order)
# class OrderResource(resources.ModelResource):
#     # https://django-import-export.readthedocs.io/en/latest/getting_started.html
#     class Meta:
#         model = Order

# @admin.register(Order)
# class OrderAdmin(ImportExportModelAdmin):
#     '''Admin View for Order'''
#     resource_class = OrderResource

#     list_display = ('title','created_date', 'deadline')
#     list_filter = ('created_date',)
#     search_fields = ('title',)

#     ordering = ('created_date',)