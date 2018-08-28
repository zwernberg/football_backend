from django.core.cache import cache


from season.models import Season
import backend.settings as settings
from owners.serializers import OwnerSerializer
from espn import service

def fetchOwners(seasonId=settings.SEASON_ID):
    result = {
        'data': {
            "divisions": {
                "1507319": [
                    {
                        "teamId": 1,
                        "owner": "Kensey Schultz"
                    },
                    {
                        "teamId": 2,
                        "owner": "neal schumacher"
                    },
                    {
                        "teamId": 3,
                        "owner": "zach Wernberg"
                    },
                    {
                        "teamId": 4,
                        "owner": "Emily Wernberg"
                    },
                    {
                        "teamId": 5,
                        "owner": "Rob Wernberg"
                    },
                    {
                        "teamId": 6,
                        "owner": "Douglas Schumacher"
                    },
                    {
                        "teamId": 7,
                        "owner": "Benjamin Wernberg"
                    },
                    {
                        "teamId": 8,
                        "owner": "Tim Schultz"
                    },
                    {
                        "teamId": 9,
                        "owner": "Tyler Schumacher"
                    },
                    {
                        "teamId": 10,
                        "owner": "Matt Stellick"
                    },
                    {
                        "teamId": 11,
                        "owner": "Kathleen Schumacher"
                    },
                    {
                        "teamId": 12,
                        "owner": "Brian Schultz"
                    }
                ],
                "1477590": [
                    {
                        "teamId": 1,
                        "owner": "Evan Schumacher"
                    },
                    {
                        "teamId": 2,
                        "owner": "Alex Haskins"
                    },
                    {
                        "teamId": 3,
                        "owner": "Ned Schumacher"
                    },
                    {
                        "teamId": 4,
                        "owner": "Tony Schumacher"
                    },
                    {
                        "teamId": 5,
                        "owner": "Luke Wernberg"
                    },
                    {
                        "teamId": 6,
                        "owner": "Ariana Smith"
                    },
                    {
                        "teamId": 7,
                        "owner": "Sally Schumacher"
                    },
                    {
                        "teamId": 8,
                        "owner": "Ryan Schumacher"
                    },
                    {
                        "teamId": 9,
                        "owner": "Sam Wernberg"
                    },
                    {
                        "teamId": 10,
                        "owner": "Nikki Gottleib"
                    },
                    {
                        "teamId": 11,
                        "owner": "Cathy Wernberg"
                    },
                    {
                        "teamId": 12,
                        "owner": "Karlyn Schumacher"
                    }
                ]
            }
        },
        'status': 200
    }
    return result