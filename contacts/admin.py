from django.contrib import admin
from contacts.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at')
    list_filter = ('is_helium', 'is_painted', 'is_metallic', 'is_foil', 'created_at')
    search_fields = ('name', 'phone', 'message')
    date_hierarchy = 'created_at'
