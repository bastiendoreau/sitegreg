# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from models import Creation

##################
# VUE index.html
##################
def index(request):
    print("test")
    return render(request, 'ebenist/index.html')#, {'creations': creations})
    
def contact(request):
    print ('contact')
    return render(request, 'ebenist/contact.html')
    
def avendre(request):
    creations = Creation.objects.filter(dispo = True)
    print("a vendre ", len(creations))
    return render(request, 'ebenist/avendre.html', {'creations': creations})
    
def galerie(request):
    creations = Creation.objects.all()
    print("galerie ", len(creations))
    return render(request, 'ebenist/galerie.html', {'creations': creations})
