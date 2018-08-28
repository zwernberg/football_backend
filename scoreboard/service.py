from owners.service import fetchOwners

def addOwners(result):
    owners = fetchOwners()
    for division in result['data']['divisions']:
        divisionId = division['metadata']['leagueId']
        for matchup in division['scoreboard']['matchups']:
            for team in matchup['teams']:
                teamIndex = (team['team']['teamId'] - 1)
                team['team']['owner'] = owners['data']['divisions'][divisionId][teamIndex]['owner']
    return result