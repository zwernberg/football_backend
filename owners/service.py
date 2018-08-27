from django.core.cache import cache


from season.models import Season
import backend.settings as settings
from owners.serializers import OwnerSerializer
from espn import service

def fetchOwners(seasonId=settings.SEASON_ID):
    if not cache.get('owners'):
        season = Season.objects.get(year=seasonId)
        divisions = season.divisions.all()

        result = {
            'data': {
                'divisions': {}
            },
            'status': ''
        }
        for division in divisions:
            r = service.fetch('teams', division.leagueId, seasonId)
            res = r.json()
            val = res['teams']
            owner_serialized = OwnerSerializer(val, many=True)
            result['data']['divisions'][division.leagueId] = owner_serialized.data
            result['status'] = r.status_code

        cache.set('owners', result, 600)
    return cache.get('owners')
