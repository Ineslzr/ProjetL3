from django import forms
from django.forms import fields
from .models import Beneficiaire, Presence, Categorie, Produit

class BeneficiaireForm(forms.ModelForm):
    class Meta:
        model = Beneficiaire
        fields = ["nom","prenom","email","telephone","code_postal","ville","adresse","nb_parts","mot_mairie","carte_donne","remarque"]

class PresenceForm(forms.ModelForm):
    class Meta:
        model = Presence
        fields= ["id_beneficiaire","date"]

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'
