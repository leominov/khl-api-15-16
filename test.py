# -*- coding: utf-8 -*-

from main import KHLAPI

tournamentId = 309

api = KHLAPI(tournamentId)
teams = api.getTeamList()

if not teams:
    exit()

for team in teams:
    print '{0};{1};{2};{3}'.format(team['rankLeague'], team['nameEn'], team['gp'], team['pts'])
