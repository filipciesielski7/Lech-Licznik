from datetime import datetime


def getDate(timestamp):
    date_obj = datetime.strptime(timestamp[:23], '%Y-%m-%dT%H:%M:%S.%f')
    date = date_obj.strftime('%Y-%m-%d %H:%M:%S')
    return date


"""
    timestamp = '2023-04-11T16:52:01.7818696'
    date = '2023-04-11 16:52:01'
"""


def stand_name(stand):
    if stand == 1:
        return 'I im. T. Anioły'
    elif stand == 2:
        return 'II Kocioł'
    elif stand == 3:
        return 'III im. H. Czapczyka'
    elif stand == 4:
        return 'IV im. E. Białasa'
    