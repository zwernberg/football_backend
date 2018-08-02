# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.cache import cache_page
from rest_framework import status
import requests
 
import backend.settings as settings

from season.models import Season
import season.serializers

from espn import service

import pdb

# Create your views here.


@cache_page(60 * 5)
@api_view(['GET',])
def league_settings(request, seasonId, leagueId):
    r = service.fetch('leagueSettings', leagueId, seasonId)
    status = r.status_code
    data = r.json()

    return Response(data, status)

@cache_page(60 * 5)
@api_view(['GET',])
def season_overview(request, seasonId):
    season = Season.objects.get(year=seasonId)
    divisions = season.divisions.all()

    data = {
        'divisions': {}
    }
    status = ""
    for division in divisions:
        r = service.fetch('leagueSettings', division.leagueId, seasonId)
        data['divisions'][division.leagueId] = r.json()
        status = r.status_code

    return Response(data, status)