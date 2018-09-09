"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin

import season.views
import team.views
import scoreboard.views
import owners.views
import standings.views

urlpatterns = [
    url(r'^api/admin/', admin.site.urls),
    url(r'^api/chat/', include('chat.urls')),
    path('api/leagueSettings/<int:seasonId>/<int:leagueId>/', season.views.league_settings,),
    path('api/seasonOverview/<int:seasonId>', season.views.season_overview,),
    path('api/scoreboard', scoreboard.views.scoreboard_view,),
    path('api/scoreboard/<int:seasonId>', scoreboard.views.scoreboard_view,),
    path('api/boxscore/<int:leagueId>/<int:matchupPeriodId>/<int:teamId>',scoreboard.views.boxscore_view,),
    path('api/owners', owners.views.owners_view,),
    path('api/standings', standings.views.standings_view,),
    path('api/team/<int:seasonId>/<int:leagueId>/<int:teamId>', team.views.team_view,)
]
