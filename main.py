import os,subprocess
os.system("pip install undetected-chromedriver==3.5.3")
os.system("pip install discord.py==2.1.0")
import requests
import threading
import time
from subprocess import Popen, PIPE
def cloud_flared():
  run = True
  cmd = "cloudflared tunnel --url http://localhost:3333 --no-autoupdate"
  with Popen(cmd,
             stdout=PIPE, universal_newlines=True) as process:
      for line in process.stdout:
          print(line)

th = threading.Thread(target=cloud_flared)
th.start()
time.sleep(5)
from flask import Flask

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'Pong!'

app.run(port=3333)


