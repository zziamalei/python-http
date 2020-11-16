import RequestUtil
import hashlib,base64
import json
import SystemLog
import time
import _thread

def getDoor():
    data ={
            "clientId": "89788097",
            "data": "{\"sys_id\":\"002dddf8-3da4-4bcb-abb9-47bb1e704fc4\",\"commandCode\":101011,\"door_no\":\"\",\"page_now\":0,\"page_size\":10}",
            "timeout": 10
            }
    try:
       response = RequestUtil.postJson('/request',data)
       if response['resultCode']=="SUCCESS":
          SystemLog.info(json.dumps(response))
       else:
          SystemLog.error(json.dumps(response))  
       
    except Exception:
       SystemLog.error("请求异常")        
    

while True:
    
    num=0
    while num<50:
       num+=1
       _thread.start_new_thread(getDoor)

    time.sleep(1)   
      
   