from django.contrib import admin
from .models import Group, User, Message

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('content', 'group', 'sender', 'timestamp', 'is_read')
    list_filter = ('group', 'sender', 'is_read')
    search_fields = ('content', 'sender__name')

    # Customize the form fields and layout if needed
    fields = ('group', 'sender', 'content', 'link', 'photo', 'is_read', 'timestamp')
    readonly_fields = ('timestamp',)

    # Customize the list view ordering if needed
    ordering = ('-timestamp',)