import urllib
import requests
import time
import os
import sys

os.system("clear")
logo = """  \u001b[31m
  __  __           _         _   _      _
 |  \/  | __ _ ___| | __    | | | |_ __| |
 | |\/| |/ _` / __| |/ /____| | | | '__| |
 | |  | | (_| \__ \   <_____| |_| | |  | |
 |_|  |_|\__,_|___/_|\_\     \___/|_|  |_|

\u001b[34m#####git:https://github.com/Jokergazaa####
  ######IG:AHM7D Sy ########
      ########J O K E A R - A ###########
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
	 follow me on github for more 	
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
	\u001b[36mpress CTRL + Z to exit
"""
key = '851331661a70a921cb67ba0f5abb5e4e844b8'
print (logo)

url = input("\u001b[33mENTER URL >>")
name  = input("\u001b[35mGIVE NAME 4 URL>>")
r = requests.get('http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(key, url, name))
data = r.json()

try:

 short = data['url']['shortLink']
 status = data['url']['status']
 print ("\n")
 print (" \u001b[31mShortening link.......")
 print ("\n")
 time.sleep(4)
 print ("\n")

 print ('link:', short)
 print ("\n")
 print ("\n")


except:
 status = data["url"]["status"]
if status == 1:
 print ("Error: The link has already been shortened")

elif status == 2:
 print ("Error:the entered link is not a link")

elif status == 3:
 print ("Error: link name is already taken try another")

elif status == 6:
 print ("The link name provided is invalid")

elif status == 6:
 print ("The link provided is from a blocked domain")

ext = input("\u001b[33mPress ENTER to continue")
print ("\n")

print ("\u001b[32m DONT FORGET TO FOLLOW ME ON GITHUB")

time.sleep(2)
sys.exit(1)
