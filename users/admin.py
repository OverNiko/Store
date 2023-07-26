from django.contrib import admin

from users.models import User
from products.admin import BasketAdminInline


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('last_login', 'date_joined',)
    inlines = (BasketAdminInline,)