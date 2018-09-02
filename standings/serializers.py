from rest_framework import serializers
import pdb

class RecordSerializer(serializers.Serializer):
    overallLosses = serializers.IntegerField()
    overallPercentage = serializers.IntegerField()
    overallStanding = serializers.IntegerField()
    overallTies = serializers.IntegerField()
    overallWins = serializers.IntegerField()
    pointsAgainst = serializers.IntegerField()
    pointsFor = serializers.IntegerField()
    streakLength = serializers.IntegerField()
    streakType = serializers.IntegerField()


class StandingSerializer(serializers.Serializer):
    teamLocation = serializers.CharField(max_length=200)
    teamId = serializers.IntegerField()
    teamNickname = serializers.CharField()
    teamAbbrev = serializers.CharField()
    rank = serializers.CharField()
    overallStanding = serializers.CharField()
    owner = serializers.SerializerMethodField()
    record = RecordSerializer()


    def get_teamName(self, obj):
        return (obj['teamLocation'] + " " + obj['teamNickname'])

    def get_owner(self, obj):
        # pdb.set_trace()
        print(obj['owner'])
        return obj['owner'] or 'not found'
