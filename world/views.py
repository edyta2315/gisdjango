# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import WorldBorders

from django.core.serializers import serialize

def index(request, fips):
    border = WorldBorders.objects.filter(fips=fips.upper())
    geojson = serialize('geojson', border, geometry_field='geom', fields=('fips', 'name', 'pop2005','area', ))
    return render (request, 'index.html',{'geojson':geojson})

