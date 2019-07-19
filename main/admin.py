from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import MyUser

# Register your models here.


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm

    list_display = ('login','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields':('login','password', 'avatar')}),
        ('Permissions', {'fields':('is_admin',)})
    )
    add_fieldsets = (None, {
            'classes': ('wide',),
            'fields': ('login', 'password1', 'password2'),
        }),
    search_fields = ('login',)
    ordering = ('login',)
    filter_horizontal = ()

admin.site.register(MyUser, MyUserAdmin)
admin.site.unregister(Group)