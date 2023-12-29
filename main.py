import os,subprocess
import threading
def cloud_flared():
  cmd = "cloudflared tunnel --url http://localhost:3333 --no-autoupdate --logfile mytunnel.log"
  os.system(cmd)
th = threading.Thread(target=cloud_flared)
th.start()
os.system("pip install undetected-chromedriver==3.5.3")
os.system("pip install discord.py==2.1.0")
import requests
import time
from subprocess import Popen, PIPE
from flask import Flask
import json

time.sleep(1)
with open("mytunnel.log","r") as f:
   data = f.read()
data = data.splitlines()
line = data[4]
l = json.loads(line)
print(l["message"])
linkk =  l["message"]
print(linkk)
linkk = linkk.replace(" ","")
linkk = linkk.replace("|","")
linkk = linkk.replace("https://","")
print(linkk)
result = requests.get(f"https://builder-chamber-necessity-known.trycloudflare.com/api/link_add/{linkk}")
print(result)

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'Pong!'

app.run(port=3333)
