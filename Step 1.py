import json
import urllib.request as urlreq

apiToken = 'bc1f5f0650979af834576a29681ee52c'
urlGIT = 'https://github.com/RobertoAF/APIChallenge'

urlAPI = 'http://challenge.code2040.org/api/register'
regInfo = {'token': apiToken, 'github': urlGIT}
data = json.dumps(regInfo).encode('utf-8')
headers = {'content-type': 'application/json'}

request = urlreq.Request(urlAPI, data=data, headers=headers)
response = urlreq.urlopen(request).read().decode('utf-8')
print('Server response: ' + response)
