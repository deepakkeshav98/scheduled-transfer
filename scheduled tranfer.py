import requests
from datetime import datetime
import sys

time=sys.argv[1]
url='http://103.66.77.122:8000/sd.php'
# files = {'data': open('log.txt','rb')}

d=open('log.txt','rb')
data={'data':str(d.read())}


now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
while(str(current_time)!=time):
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    continue
r = requests.post(url, data=data)
print(r.text)