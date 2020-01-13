from django.contrib import admin
from .models import User

# admin.site.register(User)

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    """ Custom User Admin """
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
        "email_verified",
        "email_secret",
        "login_method",
    )
    list_filter = ("superhost", "language", "currency")