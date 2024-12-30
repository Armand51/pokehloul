from django.contrib import admin
from django.utils.html import format_html
from Pokedata.models import Pokemon, Talent, Attaque

# Register your models here.

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Affiche une colonne avec l'image dans la liste des objets
    readonly_fields = ('link_clickable', 'display_image')  # Ajoute une image visible dans la vue détaillée

    def link_clickable(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.url, obj.url)
    link_clickable.short_description = "Accéder à la page"

    def display_image(self, obj):
        if obj.picture_url:  # Vérifiez que picture_url n'est pas vide
            return format_html(
                '<img src="{}" style="max-width: 200px; max-height: 200px; width: auto; height: auto;" />', 
                obj.picture_url
            )
        return "Pas d'image"
    display_image.short_description = "Image"
    

class AttaqueAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class TalentAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Talent,TalentAdmin)
admin.site.register(Attaque,AttaqueAdmin)