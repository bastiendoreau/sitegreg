# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from datetime import datetime

@python_2_unicode_compatible
class Categorie(models.Model):

    class Meta:
        db_table = 'categorie'
        verbose_name = _('categorie')
        verbose_name_plural = _('categories')
    nom_categ = models.CharField(max_length=10, default='none', verbose_name=_("Nom categorie"))
    
    def __str__(self):
        return self.nom_categ
        

@python_2_unicode_compatible
class Creation(models.Model):

    class Meta:
        db_table = 'creation'
        verbose_name = _('creation')
        verbose_name_plural = _('creations')
    titre = models.CharField(max_length=40, default='-', verbose_name=_("Titre"))
    fk_categ = models.ForeignKey('Categorie',  verbose_name=_("Categorie"), related_name='fk_categ', default=1)
    prix = models.IntegerField(verbose_name=_("Prix"), default=100)
    description = models.TextField(default='-', verbose_name=_("Description"), null=True, blank=True)
    date_fab = models.DateField(verbose_name=_("Date fabrication"), default=datetime.today)
    dispo = models.BooleanField(verbose_name=_("Disponible"), default=True)
    photo1 = models.ImageField(upload_to="photos", blank=True, null=True)
    photo2 = models.ImageField(upload_to="photos", blank=True, null=True)
    photo3 = models.ImageField(upload_to="photos", blank=True, null=True)
    #manager2 = models.ForeignKey('person.Person',  verbose_name=_("second responsable de theme"), related_name='manager2', null=True, blank=True)

    def __str__(self):
        return self.titre
        
