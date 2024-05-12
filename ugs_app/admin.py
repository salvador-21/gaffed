from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.http.request import HttpRequest
from .models import UserAccount,UserWallet,Games,Fight
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class UserAccountLine(admin.StackedInline):
    model=UserAccount
    can_delete=False
    verbose_name_plural='useraccount'
    fk_name='user'

class CustomUserAccountAdmin(UserAdmin):
    inlines=(UserAccountLine,)

admin.site.register(Games)
admin.site.register(Fight)
admin.site.unregister(User)
admin.site.register(User, CustomUserAccountAdmin)
admin.site.register(UserWallet)
