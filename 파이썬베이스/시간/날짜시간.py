import time
print(time.time())
print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))
