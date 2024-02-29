from django.contrib import admin

from appointments import models


# Register your models here.

# admin.site.register(models.PracticeArea)

@admin.register(models.PracticeArea)
class PracticeAreaAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Name", {"fields": ("name", )}),
        ("Description", {"fields": ("description", )}),
    )
