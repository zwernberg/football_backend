import backend.settings as settings
import requests

def fetch(endpoint, leagueId, seasonId = settings.SEASON_ID, extra_params = {}):
    params = {
        'leagueId' : leagueId,
        'seasonId': seasonId
    }
    params.update(extra_params)
    return requests.get(settings.ENDPOINT + endpoint, params=params)



def fetchWeek(divisions, matchupPeriodId = '', seasonId = settings.SEASON_ID):
    data = {
        'divisions': [],
    }
    status_code = ''

    for division in divisions:
        params = {
            'matchupPeriodId': matchupPeriodId
        }

        res = fetch('scoreboard', division.leagueId, seasonId, extra_params = params)
        val = res.json()
        val['metadata']['division'] = division.name
        
        data['divisions'].append(val)
        status_code = res.status_code
    return {
        'data': data,
        'status_code': status_code
    }

def fetchStandings(divisions):
    data = {
        'divisions': [],
    }
    status_code = ''

    for division in divisions:
        res = fetch('leagueSettings', division.leagueId)
        val = res.json()
        val['metadata']['division'] = division.name
        stripped = {
            'metadata': val['metadata'],
            'teams': val['leaguesettings']['teams'],
        }
        data['divisions'].append(stripped)
        status_code = res.status_code
    return {
        'data': data,
        'status_code': status_code
    }