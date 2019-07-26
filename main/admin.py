from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *

# Register your models here.


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm

    list_display = ('login','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields':('login','password')}),
        ('User information', {'fields':('name','sur_name','fath_name','age','city','avatar','link')}),
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
admin.site.register(Article)
admin.site.register(Comment)
admin.site.unregister(Group)