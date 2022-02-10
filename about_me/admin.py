from django.contrib import admin
from .models import Profile, SocialNetwork


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "user",
        "birthdate",
    )

@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "profile",
    )
