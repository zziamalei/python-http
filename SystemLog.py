import time

def info(value):
    day = time.strftime("%Y-%m-%d", time.localtime())
    f= open("log-info"+day+".txt","a+",encoding='utf-8')
    f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"->"+value+"\r\n") 
    f.flush()
def error(value):
    day = time.strftime("%Y-%m-%d", time.localtime())
    f= open("log-error"+day+".txt","a+",encoding='utf-8')
    f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"->"+value+"\r\n") 
    f.flush()