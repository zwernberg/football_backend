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
from owners.service import fetchOwners
from espn import service

TWENTY_FOUR_HOURS = 60 * 60* 24

@cache_page(TWENTY_FOUR_HOURS)
@api_view(['GET',])
def owners_view(request, seasonId=settings.SEASON_ID):
    result = fetchOwners(seasonId)
    return Response(result['data'], result['status'])