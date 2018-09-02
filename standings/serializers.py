from rest_framework import serializers

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
    overallStanding = serializers.IntegerField()
    owner = serializers.CharField()
    record = RecordSerializer()


    def get_teamName(self, obj):
        return (obj['teamLocation'] + " " + obj['teamNickname'])