import os,subprocess
os.system("pip install undetected-chromedriver==3.5.3")
os.system("pip install discord.py==2.1.0")
import requests
import threading
import time
from subprocess import Popen, PIPE
from flask import Flask
import json

def cloud_flared():
  cmd = "cloudflared tunnel --url http://localhost:3333 --no-autoupdate --logfile mytunnel.log"
  os.system(cmd)

th = threading.Thread(target=cloud_flared)
th.start()
time.sleep(5)
with open("mytunnel.log","r") as f:
   data = f.read()

data = data.splitlines()
line = data[4]
l = json.loads(line)
print(l["message"])


app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'Pong!'

app.run(port=3333)
