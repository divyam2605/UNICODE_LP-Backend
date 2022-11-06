from django.contrib import admin
from .models import Task

class taskAdmin(admin.ModelAdmin):
  list_display =['task_name', 'description', 'completion_date']

admin.site.register(Task, taskAdmin)

