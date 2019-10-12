from django.contrib             import admin

from import_export              import resources
from import_export.admin        import ImportExportModelAdmin

from selectelhackaton.coreApp.models import Order, Task, Squad
# Register your models here.

# admin.site.register(Order)
class OrderResource(resources.ModelResource):
    # https://django-import-export.readthedocs.io/en/latest/getting_started.html
    class Meta:
        model = Order

class TaskResource(resources.ModelResource):
    class Meta:
        model = Task

class SquadResource(resources.ModelResource):
    class Meta:
        model = Squad

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    '''Admin View for Order'''
    resource_class = OrderResource

    list_display = ('title','created_date', 'deadline')
    list_filter = ('created_date',)
    search_fields = ('title',)

    ordering = ('created_date',)

@admin.register(Task)
class TaskAdmin(ImportExportModelAdmin):
    '''Admin View for Task'''

    resource_class = TaskResource

    list_display = (
        'title', 
        'created_date', 
        'description', 
        'deadline', 
        'tags', 
        'updated_data', 
        'author', 
        'is_internal',
        'status'
        )

    list_filter = ('created_date', 'is_internal')

    search_fields = ('title',)

    ordering = ('created_date',)


@admin.register(Squad)
class SquadAdmin(ImportExportModelAdmin):
    '''Admin View for Squad'''
    resource_class = SquadResource

    list_display = ('id','description','teammate_str')
    list_filter = ('id',)
    search_fields = ['id',]

    ordering = ('id',)