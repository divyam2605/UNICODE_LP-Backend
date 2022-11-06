from django.contrib import admin
from .models import User
# Register your models here.

admin.site.site_header = "To Do List Admin"

class userAdmin(admin.ModelAdmin):
  list_display =['email', 'full_name', 'active', 'admin', 'staff']
  title = ['full_name', 'email', 'active', 'admin', 'staff']

admin.site.register(User, userAdmin)
#admin.site.unregister(User)


