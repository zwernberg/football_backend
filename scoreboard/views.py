from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.cache import cache_page

from espn import service
from backend import settings
from season.models import Season, Division

import pdb
# Create your views here.

#@cache_page(20)
@api_view(['GET',])
def scoreboard_view(request, seasonId=settings.SEASON_ID):
    season = Season.objects.get(year=seasonId)
    divisions = season.divisions.all()
    matchupPeriodId = request.GET.get('matchupPeriodId', '')
    response = service.fetchWeek(divisions, matchupPeriodId, seasonId)
    return Response(response['data'], response['status_code'])