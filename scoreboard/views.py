from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.cache import cache_page

from espn import service
from backend import settings
from season.models import Season, Division

from scoreboard.service import addOwners
# Create your views here.

@cache_page(30)
@api_view(['GET',])
def scoreboard_view(request, seasonId=settings.SEASON_ID):
    season = Season.objects.get(year=seasonId)
    divisions = season.divisions.all()
    matchupPeriodId = request.GET.get('matchupPeriodId', '')
    response = service.fetchWeek(divisions, matchupPeriodId, seasonId)
    result = addOwners(response)
    return Response(result['data'], result['status_code'])


@cache_page(10)
@api_view(['GET',])
def boxscore_view(request, leagueId, matchupPeriodId, teamId):
    response = service.fetchBoxscore(leagueId, matchupPeriodId, teamId)
    return Response(response['data'], response['status_code'])