from django.contrib import admin
from .models import UploadFile


class UploadFileAdmin(admin.ModelAdmin):
    # Define which fields to display in the admin list view
    list_display = ('file_name', 'uploaded_at', 'last_modified')

    # Make the 'file_name' clickable in the list view
    list_display_links = ('file_name',)

    # Remove 'last_modified' from list_editable, as it's not manually editable
    list_editable = ()  # No fields in list_editable for now

    # Allow search by file_name
    search_fields = ('file_name',)

    # Add filters based on date fields
    list_filter = ('uploaded_at', 'last_modified')


# Register the model in the admin
admin.site.register(UploadFile, UploadFileAdmin)
