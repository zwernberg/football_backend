# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.cache import cache_page
from rest_framework import status
import requests
 
import backend.settings as settings

from team.serializers import TeamSerializer

from season.models import Season
import season.serializers

from espn import service

# Create your views here.


#@cache_page(60 * 5)
@api_view(['GET',])
def league_settings(request, seasonId, leagueId):
    r = service.fetch('leagueSettings', leagueId, seasonId)
    data = r.json()

    val = data['leaguesettings']['teams'].values()
    team_serialized = TeamSerializer(val, many=True)
    data['leaguesettings']['teams'] = team_serialized.data
    status = r.status_code
    

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
        r = service.fetch('teams', division.leagueId, seasonId)
        data['divisions'][division.leagueId] = r.json()
        status = r.status_code

    return Response(data, status)