# -*- coding: utf-8 -*-

from main import KHLAPI

api = KHLAPI()
tournaments = api.getAllTournaments()

if not tournaments:
    exit()

for tournament in tournaments:
    print "{0}\t{1}\t{2}".format(tournament["tournamentID"], tournament["eventNameEn"], tournament['logoEn'])

    api.setTournament(tournament["tournamentID"])
    teams = api.getTeamList()

    if not teams:
        continue

    for team in teams:
        print "\t{0}\t{1}".format(team["rankLeague"], team["nameEn"])
