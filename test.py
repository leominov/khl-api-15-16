# -*- coding: utf-8 -*-

from main import KHLAPI


def main(with_players):
    api = KHLAPI()
    tournaments = api.getAllTournaments()

    if not tournaments:
        exit()

    for tournament in tournaments:
        print "{0}\t{1}\t{2}".format(tournament["tournamentID"], tournament["eventNameEn"], tournament['logoEn'])

        teams = api.\
            setTournament(tournament["tournamentID"]).\
            getTeamList()

        if not teams:
            continue

        for team in teams:
            print "\t{0}\t{1}".format(team["rankLeague"], team["nameEn"])

            if not with_players:
                continue

            players = api.\
                getTeamMembers(team["id"])

            if not players:
                continue

            for player in players:
                print "\t\t{0}\t{1}\t{2}".format(player["nameEn"], player["birthday"], player["imageUrl"])

main(with_players=False)
