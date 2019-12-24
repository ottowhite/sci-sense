from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin


# register your models here
class UserAdmin(DefaultUserAdmin):
    list_display = ('email', 'date_of_birth', 'date_joined', 'last_login', 'is_staff', 'is_admin')
    search_fields = ('email', )
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, UserAdmin)