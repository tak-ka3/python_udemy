import requests

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post('http://httpbin.org/post',data=payload, timeout=1)

print(r.status_code)
print(r.text)
print(r.json())