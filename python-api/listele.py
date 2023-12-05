import requests

reqUrl = "http://127.0.0.1:6767/users"

headersList = {
 "Accept": "/",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)"
}

payload = ""

response= requests.request("GET", reqUrl, data=payload, headers=headersList)

print(response.text)