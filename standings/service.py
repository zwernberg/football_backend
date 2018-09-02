from owners.service import fetchOwners
from team.serializers import TeamSerializer

def addOwners(data):
    owners = fetchOwners()
    for division in data['divisions']:
        divisionId = division['metadata']['leagueId']

        for i in range(1, len(division['teams']) + 1):
            team = division['teams'][str(i)]
            teamIndex = (team['teamId'] - 1)
            team['owner'] = owners['data']['divisions'][divisionId][teamIndex]['owner']
    return data


def serializeWithOwners(data):
    for division in data['divisions']:
        val = division['teams'].values()
        team_serialized = TeamSerializer(val, many=True)
        division['teams'] = team_serialized.data

    data = addOwners(data)
    return data
