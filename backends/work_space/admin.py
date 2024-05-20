# work_space/admin.py
from django.contrib import admin
from .models import WorkSpace


class WorkSpaceAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'address',
                    'opening_date',
                    'type_workspace',
                    'director')
    search_fields = ('title',
                     'address',
                     'type_workspace',
                     'director__username')
    list_filter = ('type_workspace',)


admin.site.register(WorkSpace, WorkSpaceAdmin)
