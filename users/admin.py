from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.

User = get_user_model()

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email", "image_url", "is_superuser", "is_staff"]
    search_fields = ["name"]