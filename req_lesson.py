import urllib.request
import json

payload = {'key1': 'value1', 'key2': 'value2'}
url1 = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
print(url1)

url = 'http://httpbin.org/get'
with urllib.request.urlopen(url) as f:
  # print(f.read().decode('utf-8'))
  print('#############')
  r = json.loads(f.read().decode('utf-8'))
  print(r)

payload = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
  'http://httpbin.org/post', data=payload, method='POST'
)
with urllib.request.urlopen(req) as f:
  print(json.loads(f.read().decode('utf-8')))
