import backend.settings as settings
import requests

def fetch(endpoint, leagueId, seasonId = settings.SEASON_ID, extra_params = {}):
    params = {
        'leagueId' : leagueId,
        'seasonId': seasonId
    }
    params.update(extra_params)
    return requests.get(settings.ENDPOINT + endpoint, params=params)