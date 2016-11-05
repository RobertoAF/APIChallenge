import json
import urllib.request as urlreq

apiToken = 'bc1f5f0650979af834576a29681ee52c'
HTTP = 'http://challenge.code2040.org/api/reverse'
info = {'token': apiToken}
data = json.dumps(info).encode('utf-8')
headers = {'content-type': 'application/json'}

revRequest = urlreq.Request(HTTP, data=data, headers=headers)
revResponse = urlreq.urlopen(revRequest).read().decode('utf-8')

reverseString = revResponse[::-1]

valHTTP = 'http://challenge.code2040.org/api/reverse/validate'
valInfo = {'token': apiToken, 'string': reverseString}
valData = json.dumps(valInfo).encode('utf-8')

valRequest = urlreq.Request(valHTTP, data=valData, headers=headers)
valResponse = urlreq.urlopen(valRequest).read().decode('utf-8')
print('Server response: ' + valResponse)
