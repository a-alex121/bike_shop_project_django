from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Numele categoriei")
    description = models.TextField(blank=True, null=True, help_text="Descrierea categoriei")
    color = models.CharField(max_length=30, default="#4B5563", help_text="Culoarea categoriei pentru UI")

    class Meta:
        ordering = ["name"]
        verbose_name = "Categorie"
        verbose_name_plural = "Categorii"

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Numele brandului")
    country = models.CharField(max_length=100, blank=True, null=True, help_text="Țara de origine")
    website = models.URLField(blank=True, null=True, help_text="Site-ul oficial")

    class Meta:
        ordering = ["name"]
        verbose_name = "Brand"
        verbose_name_plural = "Branduri"

    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS_CHOICES = [
        ("available", "Disponibil"),
        ("unavailable", "Indisponibil"),
        ("limited", "Stoc limitat"),
    ]

    name = models.CharField(max_length=200, unique=True, help_text="Numele produsului")
    slug = models.SlugField(max_length=200, unique=True, blank=True, help_text="Identificator URL")
    description = models.TextField(help_text="Descriere detaliată a produsului")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Prețul produsului")
    stock = models.PositiveIntegerField(default=0, help_text="Cantitatea disponibilă")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products", help_text="Categoria produsului")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name="products", help_text="Brandul produsului")
    image = models.URLField(blank=True, null=True, help_text="Imagine principală a produsului")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Data și ora creării")
    updated_at = models.DateTimeField(auto_now=True, help_text="Data și ora ultimei modificări")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="available", help_text="Starea produsului")

    class Meta:
        ordering = ["name"]
        verbose_name = "Produs"
        verbose_name_plural = "Produse"

    def __str__(self):
        return self.name
