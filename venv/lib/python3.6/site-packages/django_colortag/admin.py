from django.contrib import admin

class ColorTagAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'slug',
        'description',
        'color',
    )
    prepopulated_fields = {
        "slug": ("name",)
    }
