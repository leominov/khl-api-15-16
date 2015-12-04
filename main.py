# -*- coding: utf-8 -*-

import requests


class KHLAPI:
    tournamentId = 0

    url = 'http://khl.egluservices.com/services/query.php'

    headers = {
        'User-Agent': 'КХЛ/3013 CFNetwork/758.0.2 Darwin/15.0.0',
    }

    base = {
        'os': 'android',
        'lang': 'ru',
    }

    def _req(self, payload):
        payload.update(self.base)
        r = requests.post(url=self.url, data=payload, headers=self.headers)

        if r.status_code != 200:
            return False

        return r.json()

    def setTournament(self, tournamentId):
        self.tournamentId = tournamentId

    def getAllTournaments(self):
        """Чемпионаты"""
        payload = {
            'requestName': 'allTournaments',
        }

        return self._req(payload)

    def getTeamList(self):
        """Команды турнира"""
        payload = {
            'requestName': 'teamList',
            'tournamentId': self.tournamentId,
        }

        return self._req(payload)

    def getTeamMembers(self, teamId):
        """Состав команды турнира"""
        payload = {
            'requestName': 'teamMembers',
            'tournamentId': self.tournamentId,
            'teamId': teamId,
        }

        return self._req(payload)
