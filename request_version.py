import requests
#test upstream

res = requests.get("https://raw.githubusercontent.com/shovo4/CMPUT404/master/request_version.py")
print(res.text)

