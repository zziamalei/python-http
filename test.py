import RequestUtil
import hashlib,base64
import json
import SystemLog
import time


def login():
    password = hashlib.md5("123456ml".encode()).hexdigest()
    loginData ={
                "password": password,
                "phone": "18825235053"
                }
    response = RequestUtil.postJson('/auth/loginByPhone',loginData)
  
    print(response)
    if(response['code']==0):
      token = response['data']['token']
      print(token)
      RequestUtil.setToken(token)
      return token
    else:
      return  
def getWallet():
    return RequestUtil.postJson('/card/getWallet',{}) 

f= open("log.txt","a+",encoding='utf-8')
while True:
   token = login()
   if not token is None :
    log =  "获取到token： %s\r\n" % (token)  
    SystemLog.info(log)
    print(getWallet())
   else:
     SystemLog.info("获取token失败\r\n")  
   
   f.flush()
   time.sleep(1)


