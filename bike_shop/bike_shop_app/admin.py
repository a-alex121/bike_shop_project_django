from django.contrib import admin
from .models import Producator, Categorie, ModelBicicleta, Sediu, Raion


@admin.register(Producator)
class ProducatorAdmin(admin.ModelAdmin):
    list_display = ["nume", "tara_origine", "site_web"]
    search_fields = ["nume", "tara_origine"]
    ordering = ["nume"]


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ["nume", "culoare", "tip_utilizare"]
    search_fields = ["nume", "descriere"]
    ordering = ["nume"]


@admin.register(ModelBicicleta)
class ModelBicicletaAdmin(admin.ModelAdmin):
    list_display = ["nume", "pret_lei", "greutate_kg", "material_cadru", "producator", "categorie"]
    search_fields = ["nume", "descriere"]
    list_filter = ["categorie", "producator", "material_cadru", "este_electrica"]
    ordering = ["nume"]
    list_per_page = 10


@admin.register(Sediu)
class SediuAdmin(admin.ModelAdmin):
    list_display = ["denumire", "adresa", "telefon"]
    search_fields = ["denumire", "adresa"]
    ordering = ["denumire"]


@admin.register(Raion)
class RaionAdmin(admin.ModelAdmin):
    list_display = ["sediu", "cod_raion", "denumire", "suprafata_mp"]
    search_fields = ["denumire", "cod_raion"]
    list_filter = ["sediu"]
    ordering = ["sediu", "cod_raion"]
