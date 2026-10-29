from django.db import models


class Producator(models.Model):
    nume = models.CharField(max_length=150, unique=True, help_text="Numele producătorului")
    tara_origine = models.CharField(max_length=100, blank=True, null=True, help_text="Țara de origine")
    site_web = models.URLField(blank=True, null=True, help_text="Site-ul oficial")

    class Meta:
        ordering = ["nume"]
        verbose_name = "Producător"
        verbose_name_plural = "Producători"

    def __str__(self):
        return self.nume


class Categorie(models.Model):
    nume = models.CharField(max_length=100, unique=True, help_text="Numele categoriei")
    descriere = models.TextField(blank=True, null=True, help_text="Descrierea categoriei")
    culoare = models.CharField(max_length=30, default="#2563EB", help_text="Culoarea reprezentativă a categoriei")
    sigla = models.CharField(max_length=255, blank=True, default="", help_text="Cale către imagine sau nume icon din bibliotecă")
    tip_utilizare = models.CharField(max_length=100, blank=True, null=True, help_text="Tipul de utilizare recomandată")
    slug = models.SlugField(max_length=120, unique=True, blank=True, help_text="Slug pentru URL")

    class Meta:
        ordering = ["nume"]
        verbose_name = "Categorie"
        verbose_name_plural = "Categorii"

    def __str__(self):
        return self.nume


class ModelBicicleta(models.Model):
    MATERIAL_CHOICES = [
        ("aluminiu", "Aluminiu"),
        ("otel", "Oțel"),
        ("carbon", "Carbon"),
        ("titan", "Titan"),
    ]

    BRAKE_CHOICES = [
        ("disc_mecanic", "Disc mecanic"),
        ("disc_hidraulic", "Disc hidraulic"),
        ("janta", "Jantă"),
    ]

    nume = models.CharField(max_length=200, help_text="Numele modelului")
    descriere = models.TextField(help_text="Descrierea modelului")
    pret_lei = models.DecimalField(max_digits=10, decimal_places=2, help_text="Prețul modelului în lei")
    greutate_kg = models.FloatField(help_text="Greutatea în kg")
    numar_viteze = models.PositiveIntegerField(help_text="Număr de viteze")
    diametru_roata_inch = models.FloatField(help_text="Diametrul roții în inch")
    material_cadru = models.CharField(max_length=20, choices=MATERIAL_CHOICES, help_text="Materialul cadrului")
    tip_frana = models.CharField(max_length=20, choices=BRAKE_CHOICES, help_text="Tipul frânei")
    este_electrica = models.BooleanField(default=False, help_text="Dacă este electrică")
    data_lansare = models.DateField(blank=True, null=True, help_text="Data lansării")
    culori_disponibile = models.JSONField(default=list, blank=True, help_text="Lista de culori disponibile")
    imagine_principala = models.URLField(blank=True, null=True, help_text="Link către imagine")

    producator = models.ForeignKey(Producator, on_delete=models.PROTECT, related_name="modele", help_text="Producătorul")
    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT, related_name="modele", help_text="Categoria modelului")

    class Meta:
        ordering = ["nume"]
        verbose_name = "Model bicicletă"
        verbose_name_plural = "Modele biciclete"

    def __str__(self):
        return self.nume


class Sediu(models.Model):
    denumire = models.CharField(max_length=150, help_text="Denumirea sediului")
    adresa = models.CharField(max_length=255, help_text="Adresa sediului")
    telefon = models.CharField(max_length=30, blank=True, null=True, help_text="Telefonul sediului")
    data_deschidere = models.DateField(help_text="Data deschiderii sediului")
    modele = models.ManyToManyField(ModelBicicleta, related_name="sedii", blank=True, help_text="Modelele comercializate în sediu")

    class Meta:
        ordering = ["denumire"]
        verbose_name = "Sediu"
        verbose_name_plural = "Sediuri"

    def __str__(self):
        return self.denumire


class Raion(models.Model):
    sediu = models.ForeignKey(Sediu, on_delete=models.CASCADE, related_name="raioane", help_text="Sediul proprietar")
    cod_raion = models.CharField(max_length=20, help_text="Codul raionului în cadrul sediului")
    denumire = models.CharField(max_length=100, help_text="Numele raionului")
    suprafata_mp = models.FloatField(help_text="Suprafața raionului în m²")

    class Meta:
        unique_together = ("sediu", "cod_raion")
        ordering = ["sediu", "cod_raion"]
        verbose_name = "Raion"
        verbose_name_plural = "Raioane"

    def __str__(self):
        return f"{self.sediu} - {self.denumire}"
