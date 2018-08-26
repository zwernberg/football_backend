# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.cache import cache_page
from rest_framework import status
import requests
 
import backend.settings as settings
from espn import service
# Create your views here.


@cache_page(60 * 5)
@api_view(['GET',])
def team_view(request, seasonId, leagueId, teamId):
    extra_params = {
        'teamIds': [ teamId ]
    }
    r = service.fetch('rosterInfo', leagueId, seasonId, extra_params)
    status = r.status_code
    data = r.json()

    return Response(data, status)