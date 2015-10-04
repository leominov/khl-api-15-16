# -*- coding: utf-8 -*-

import requests


class KHLAPI:
    url = 'http://khl.egluservices.com/services/query.php'

    headers = {
        'User-Agent': 'КХЛ/3013 CFNetwork/758.0.2 Darwin/15.0.0',
    }

    base = {
        'os': 'android',
        'lang': 'ru',
    }

    def __init__(self, tournamentId):
        self.tournamentId = tournamentId

    def _req(self, payload):
        payload.update(self.base)
        r = requests.post(url=self.url, data=payload, headers=self.headers)
        if r.status_code != 200:
            return False

        return r.json()

    def getTeamList(self):
        payload = {
            'requestName': 'teamList',
            'tournamentId': self.tournamentId,
        }

        return self._req(payload)
