import json
import urllib.request as urlreq

apiToken = 'bc1f5f0650979af834576a29681ee52c'
HTTP = 'http://challenge.code2040.org/api/haystack'
info = {'token': apiToken}
data = json.dumps(info).encode('utf-8')
headers = {'content-type': 'application/json'}

request = urlreq.Request(HTTP, data=data, headers=headers)
response = urlreq.urlopen(request).read().decode('utf-8')

dataJSON = json.loads(response)

try:
    needleIDX = dataJSON["haystack"].index(dataJSON["needle"])
except:
    pass

valHTTP = 'http://challenge.code2040.org/api/haystack/validate'
valInfo = {'token': apiToken, 'needle': needleIDX}
valData = json.dumps(valInfo).encode('utf-8')

valRequest = urlreq.Request(valHTTP, data=valData, headers=headers)
valResponse = urlreq.urlopen(valRequest).read().decode('utf-8')
print('Server response: ' + valResponse)
