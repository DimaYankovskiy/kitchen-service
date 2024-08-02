from django.contrib import admin

from kitchen.models import Cook


@admin.register(Cook)
class CookAdmin(admin.ModelAdmin):
    list_display = ("username", "years_of_experience")
    search_fields = ("username",)
    list_filter = ("years_of_experience",)
