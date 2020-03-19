import urllib.request
import urllib.parse
import ast

# Geocoder API 2.0
ApiKey = ""
x = 0.0
y = 0.0

def getLoc_x(place_address) :
    address = place_address
    apiUrl = 'http://api.vworld.kr/req/address?service=address&request=getCoord&key='+ApiKey+'&'

    values = {
    'address':address,
    'type':'ROAD'
    }

    param = urllib.parse.urlencode(values)
    Adding = apiUrl+param

    req = urllib.request.Request(Adding)
    res = urllib.request.urlopen(req)

    respon_data = res.read().decode()

    DataDict = ast.literal_eval(respon_data)

    x = DataDict['response']['result']['point']['x']
    y = DataDict['response']['result']['point']['y']

    return x

def getLoc_y(place_address) :
    address = place_address
    apiUrl = 'http://api.vworld.kr/req/address?service=address&request=getCoord&key='+ApiKey+'&'

    values = {
    'address':address,
    'type':'ROAD'
    }

    param = urllib.parse.urlencode(values)
    Adding = apiUrl+param

    req = urllib.request.Request(Adding)
    res = urllib.request.urlopen(req)

    respon_data = res.read().decode()

    DataDict = ast.literal_eval(respon_data)

    x = DataDict['response']['result']['point']['x']
    y = DataDict['response']['result']['point']['y']

    return y
