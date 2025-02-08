from django.contrib import admin

# Register your models here.
from .models import Contact, ContactAdmin

class Contact(admin.ModelAdmin):
    clist=['name', 'email', 'message']
admin.site.register(Contact, ContactAdmin);