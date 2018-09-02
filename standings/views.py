from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.cache import cache_page

from backend import settings
from season.models import Season
from espn import service

from standings.service import addOwners
from standings.serializers import StandingSerializer

TEN_MINUTES = 60 * 10

@cache_page(TEN_MINUTES)
@api_view(['GET',])
def standings_view(request):

    season = Season.objects.get(year=settings.SEASON_ID)
    divisions = season.divisions.all()
    matchupPeriodId = request.GET.get('matchupPeriodId', '')
    response = service.fetchStandings(divisions)

    addOwners(response['data'])

    for index, division in enumerate(response['data']['divisions']):
        val = division['teams'].values()
        standings_serialized = StandingSerializer(val, many=True)
        response['data']['divisions'][index]['teams'] = standings_serialized.data
    

    return Response(response['data'], response['status_code'])