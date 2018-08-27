from owners.service import fetchOwners

def addOwners(result):
    owners = fetchOwners()
    for division in result['data']['divisions']:
        divisionId = division['metadata']['leagueId']
        for matchup in division['scoreboard']['matchups']:
            for team in matchup['teams']:
                teamId = team['team']['teamId']
                for owner in owners['data']['divisions'][divisionId]:
                    if owner['teamId'] == teamId:
                        team['team']['owner'] = owner['owner']
                        break
    return result