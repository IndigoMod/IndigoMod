from requests import get


def getip():
    return get('https://api.ipify.org').text