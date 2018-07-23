# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin



from models import Creation, Categorie

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom_categ',)
    #ordering = ('name_page',)

admin.site.register(Categorie, CategorieAdmin)

class CreationAdmin(admin.ModelAdmin):
    list_display = ('titre',)
    #ordering = ('name_page',)

admin.site.register(Creation, CreationAdmin)


