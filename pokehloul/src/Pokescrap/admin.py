from django.contrib import admin
from django.utils.html import format_html
from .models import To_Scrap


class ToScrapAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_element', 'is_scraped')  # Colonnes affichées dans la liste
    list_filter = ('type_element','is_scraped')  # Ajoute un filtre basé sur le champ 'type'
    readonly_fields = ('link_clickable',)  # Ajoutez un champ en lecture seule cliquable dans la vue détaillée

    def link_clickable(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.url, obj.url)
    link_clickable.short_description = "Accéder à la page"
    
    
admin.site.register(To_Scrap, ToScrapAdmin)
