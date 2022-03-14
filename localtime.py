import time
def localtime():
    res = time.asctime(time.localtime(time.time()))
    print(res)
