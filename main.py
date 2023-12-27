import os,subprocess
os.system("pip install undetected-chromedriver==3.5.3")
os.system("pip install discord.py==2.1.0")
import requests
result = subprocess.run("cloudflared tunnel --url http://localhost:3333 --no-autoupdate",shell=False,stdout=subprocess.PIPE)
#print(result.stdout)
