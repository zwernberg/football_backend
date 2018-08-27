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
        
        # for matchup in val['scoreboard']['matchups']:
        #     players = []
        #     for team in matchup['teams']:
        #         params = {
        #             'playerId': ",".join(str(v) for v in team['playerIDs']),
        #             'useCurrentPeriodProjectedStats': True,
        #             'useCurrentPeriodRealStats': True,
        #             'includeRankings': False,
        #             'includeProjectionText': False,
        #             'includeOwnPotentialTradeTransactions': False,
        #             'includeLatestNews': False,
        #             'matchupPeriodId': matchupPeriodId
        #         }
        #         team_result = fetch('playerInfo', league.league_id, extra_params= params)
        #         players = team_result.json()['playerInfo']['players']
        #         team['players'] = players

        data['divisions'].append(val)
        status_code = res.status_code
    return {
        'data': data,
        'status_code': status_code
    }