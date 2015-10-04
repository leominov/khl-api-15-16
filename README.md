# khl-egluservices
KHL API (test)
## Endpoint
Method: POST
URL: http://khl.egluservices.com/services/query.php
## Requests
### Фотогалерея
```javascript
{
    'os': 'android',
    'lang': 'ru',
    'requestName': 'photogallery',
    'tournamentId': tournamentId
}
```
### Новости
```javascript
{
    'os': 'android',
    'lang': 'ru',
    'requestName': 'news',
    'position': 0
}
```
### Чемпионаты
```javascript
{
    'os': 'android',
    'lang': 'ru',
    'requestName': 'allTournaments'
}
```
### Таблица
```javascript
{
    'os': 'android',
    'lang': 'ru',
    'requestName': 'teamList',
    'tournamentId': tournamentId
}
```
### Игры
```javascript
{
    'os': 'android',
    'lang': 'ru',
    'requestName': 'games',
    'dateTo': '2015-10-31 19:00:00  0000',
    'dateFrom': '2015-09-30 19:00:00  0000'
}
```
### Состав
```javascript
{
    'os': 'android',
    'lang': 'ru',
    'requestName': 'teamMembers',
    'tournamentId': tournamentId,
    'teamId': teamId
}
```
### Комментарии
```javascript
{
    'os': 'android',
    'lang': 'ru',
    'requestName': 'gameComments',
    'gameId': gameId
}
```
### Игровые ситуации
```javascript
{
    'os': 'android',
    'lang': 'ru',
    'requestName': 'gameSituations',
    'gameId': gameId
}
```
### Статистика
```javascript
{
    'os': 'android',
    'lang': 'ru',
    'requestName': 'statistics',
    'tournamentId': tournamentId,
    'position': '',
    'type': 'pts'
}
```
