from rest_framework import serializers


class OwnerSerializer(serializers.Serializer):
    teamId = serializers.IntegerField()
    owner = serializers.SerializerMethodField()

    # def get_teamName(self, obj):
    #     return (obj['teamLocation'] + " " + obj['teamNickname'])

    def get_owner(self, obj):
        owner = obj['owners'][0]
        if (obj['teamAbbrev'] == 'PRIN'):
            owner = obj['owners'][1]
        return (owner['firstName'] + ' ' + owner['lastName'])