import urllib.request
import json

token = ""
domain = "http://192.168.1.152:8083"
def getToken():
    global token
    return token
def setToken(value):
    global token
    token = value
def postJson(url,data):
    global token
    print(token)
    header={
        # "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
        "Content-Type": "application/json; charset=UTF-8"
         ,"token": token
        #  ,"Origin": "http://192.168.1.24:1234"
    }
    data = json.dumps(data)
    print(data)
    data = bytes(data, 'utf-8')
    # datas=urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(domain+url,data=data,headers=header)
    resp = urllib.request.urlopen(req).read().decode('utf-8')
    return json.loads(resp)