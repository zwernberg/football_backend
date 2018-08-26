from rest_framework import serializers


class TeamSerializer(serializers.Serializer):
    teamLocation = serializers.CharField(max_length=200)
    teamId = serializers.IntegerField()
    teamNickname = serializers.CharField()
    teamAbbrev = serializers.CharField()
    teamName = serializers.SerializerMethodField()

    def get_teamName(self, obj):
        return (obj['teamLocation'] + " " + obj['teamNickname'])
