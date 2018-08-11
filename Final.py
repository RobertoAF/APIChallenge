import json
import urllib.request as urlreq
from datetime import timedelta
import iso8601

def getToken():
    return 'bc1f5f0650979af834576a29681ee52c'

def getHeaders():
    return {'content-type': 'application/json'}

def getData(info):
    return json.dumps(info).encode('utf-8')

def printResponse(response):
    print('Server response: ' + response)
 
def register(apiToken):
    urlGIT = 'https://github.com/RobertoAF/APIChallenge'
    urlRegister = 'http://challenge.code2040.org/api/register'
    info = {'token': apiToken, 'github': urlGIT}
    request = urlreq.Request(urlRegister, data=getData(info), headers=getHeaders())
    response = urlreq.urlopen(request).read().decode('utf-8')

    printResponse(response)

def reverse(apiToken):
    urlReverse = 'http://challenge.code2040.org/api/reverse'
    info = {'token': apiToken}
    revRequest = urlreq.Request(urlReverse, data=getData(info), headers=getHeaders())
    revResponse = urlreq.urlopen(revRequest).read().decode('utf-8')

    reverseString = revResponse[::-1]

    urlVal = 'http://challenge.code2040.org/api/reverse/validate'
    valInfo = {'token': apiToken, 'string': reverseString}
    valRequest = urlreq.Request(urlVal, data=getData(valInfo), headers=getHeaders())
    valResponse = urlreq.urlopen(valRequest).read().decode('utf-8')

    printResponse(valResponse)

def haystack(apiToken):
    urlHaystack = 'http://challenge.code2040.org/api/haystack'
    info = {'token': apiToken}
    request = urlreq.Request(urlHaystack, data=getData(info), headers=getHeaders())
    response = urlreq.urlopen(request).read().decode('utf-8')

    dataJSON = json.loads(response)

    try:
        needleIDX = dataJSON["haystack"].index(dataJSON["needle"])
    except:
        pass

    urlVal = 'http://challenge.code2040.org/api/haystack/validate'
    valInfo = {'token': apiToken, 'needle': needleIDX}
    valRequest = urlreq.Request(urlVal, data=getData(valInfo), headers=getHeaders())
    valResponse = urlreq.urlopen(valRequest).read().decode('utf-8')

    printResponse(valResponse)

def prefix(apiToken):
    urlPrefix = 'http://challenge.code2040.org/api/prefix'
    info = {'token': apiToken}
    request = urlreq.Request(urlPrefix, data=getData(info), headers=getHeaders())
    response = urlreq.urlopen(request).read().decode('utf-8')

    dataJSON = json.loads(response)

    noPrefixList = [item for item in dataJSON["array"] if item.startswith(dataJSON["prefix"]) is False]     

    urlVal = 'http://challenge.code2040.org/api/prefix/validate'
    valInfo = {'token': apiToken, 'array': noPrefixList}
    valRequest = urlreq.Request(urlVal, data=getData(valInfo), headers=getHeaders())
    valResponse = urlreq.urlopen(valRequest).read().decode('utf-8')

    printResponse(valResponse)

def dating(apiToken):
    urlDating = 'http://challenge.code2040.org/api/dating'
    info = {'token': apiToken}
    request = urlreq.Request(urlDating, data=getData(info), headers=getHeaders())
    response = urlreq.urlopen(request).read().decode('utf-8')

    data = json.loads(response)

    newDate = iso8601.parse_date(data["datestamp"]) + timedelta(seconds=int(data["interval"]))
    newDatestamp = newDate.isoformat()[:-6] + 'Z'
 
    urlVal = 'http://challenge.code2040.org/api/dating/validate'
    valInfo = {'token': apiToken, 'datestamp': newDatestamp}
    valRequest = urlreq.Request(urlVal, data=getData(valInfo), headers=getHeaders())
    valResponse = urlreq.urlopen(valRequest).read().decode('utf-8')

    printResponse(valResponse)

def main():
    apiToken = getToken()
    register(apiToken)
    reverse(apiToken)
    haystack(apiToken)
    prefix(apiToken)
    dating(apiToken)

main()
