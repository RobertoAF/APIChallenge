import json
import urllib.request as urlreq
from datetime import timedelta
import iso8601

apiToken = 'bc1f5f0650979af834576a29681ee52c'
HTTP = 'http://challenge.code2040.org/api/dating'
info = {'token': apiToken}
data = json.dumps(info).encode('utf-8')
headers = {'content-type': 'application/json'}

request = urlreq.Request(HTTP, data=data, headers=headers)
response = urlreq.urlopen(request).read().decode('utf-8')

data = json.loads(response)

newDate = iso8601.parse_date(data["datestamp"]) + timedelta(seconds=int(data["interval"]))

newDatestamp = newDate.isoformat()[:-6] + 'Z'
valHTTP = 'http://challenge.code2040.org/api/dating/validate'
valInfo = {'token': apiToken, 'datestamp': newDatestamp}
valData = json.dumps(valInfo).encode('utf-8')

valRequest = urlreq.Request(valHTTP, data=valData, headers=headers)
valResponse = urlreq.urlopen(valRequest).read().decode('utf-8')
print('Server response: ' + valResponse)
