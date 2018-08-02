# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

season_status = (
    (0, 'Preseason'),
    (1, 'In Season'),
    (2, 'Season Over')
)

# Models

class Season(models.Model):
    year = models.IntegerField()
    status = models.IntegerField(choices=season_status)

    def __str__(self):
        return str(self.year)

class Division(models.Model):
    season = models.ForeignKey(
        Season,
        related_name='divisions',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    leagueId = models.CharField(max_length=100)


    def __str__(self):
        return self.name
