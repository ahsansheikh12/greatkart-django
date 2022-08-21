from django.contrib import admin
from .models import ContactData
# Register your models here.
class ContactDataAdmin(admin.ModelAdmin):
    list_display=('name','email','messagenote')

admin.site.register(ContactData,ContactDataAdmin)   