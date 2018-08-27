# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.cache import cache_page
from rest_framework import status
import requests
 
import backend.settings as settings
from season.models import Season

from owners.serializers import OwnerSerializer

from espn import service

import pdb

TWENTY_FOUR_HOURS = 60 * 60* 24

@cache_page(TWENTY_FOUR_HOURS)
@api_view(['GET',])
def owners_view(request, seasonId=settings.SEASON_ID):
    season = Season.objects.get(year=seasonId)
    divisions = season.divisions.all()

    data = {
        'divisions': {}
    }
    status = ""
    for division in divisions:
        r = service.fetch('teams', division.leagueId, seasonId)
        res = r.json()
        #pdb.set_trace()
        # data['divisions'][division.leagueId] = r.json()
        val = res['teams']
        owner_serialized = OwnerSerializer(val, many=True)
        data['divisions'][division.leagueId] = owner_serialized.data
        status = r.status_code

    return Response(data, status)