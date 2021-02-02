#!/usr/bin/env python3

import sys
import os
import requests
import urllib
import wget

# static
API_KEY = ""
API_ENDPOINT_LINK = "https://api.real-debrid.com/rest/1.0/unrestrict/link"
API_ENDPOINT_FOLDER = "https://api.real-debrid.com/rest/1.0/unrestrict/folder"
HEADERS = {'Authorization': "Bearer " + API_KEY}

# getting inputs
try:
	arg=sys.argv[1]
except IndexError:
	sys.exit("Error: please input an argument")
if '.txt' in arg:
	try:
		with open(arg) as f:
			links = f.readlines()
		links = [x.strip() for x in links]
	except FileNotFoundError:
		sys.exit("Error: file not found")
else:
	links = [arg]

# converting folder to files if needed
new_links=[]
for link in links:
	if 'folder' in link:
		response = requests.post(url=API_ENDPOINT_FOLDER, headers=HEADERS, data={'link': link})
		jsonResponse = response.json()
		for file in jsonResponse:
			new_links.append(file)
	else:
		new_links.append(link)

# download all files
os.makedirs('download/', exist_ok=True)
for link in new_links:
	print('Getting link from real-debrid...')
	response = requests.post(url=API_ENDPOINT_LINK, headers=HEADERS, data={'link': link})
	jsonResponse = response.json()
	try:
		downloadUrl = jsonResponse['download']
	except KeyError:
		sys.exit("Error: " + jsonResponse['error'])
	downloadUrlunq = urllib.parse.unquote(downloadUrl)
	print('Downloading with wget...')
	wget.download(downloadUrlunq, 'download/')
	print()
print('Success!')
