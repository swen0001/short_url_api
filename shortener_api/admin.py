from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "original_link",
        "short_link",
        "counter"
    )
    list_display_links = (
        "id",
        "original_link",
    )
    search_fields = (
        "original_link",
        "short_link",
    )


admin.site.register(Link, LinkAdmin)
