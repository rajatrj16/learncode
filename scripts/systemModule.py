import os, datetime, time
import re

pwd = os.getcwd()
print(pwd)
dir = 'system'
addpath = os.path.join(pwd, dir)
if not os.path.exists(dir):
    os.mkdir(addpath)
    print(os.listdir(pwd))
    print("if not statement")
else:
    rmv = os.rmdir(dir)
    print("else statement")

for i in range(1):
    # time.sleep(1)
    t = datetime.datetime.now()
    print (t.time())
    print (t.strftime("%B"))

touch = 'filename.txt'
file = open(touch, 'w')
file.write("this is text file")
file.close()
f = open(touch, 'r')
text = f.read()
print(text)
f.close()
