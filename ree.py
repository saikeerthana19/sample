import requests
import html
r = requests.get()
if r.status_code == 200:
currentMatches = r.json()[“data”]
#for match in currentMatches:
#	print(html.unescape(match[“title”]))
#lse:
#	print(“Error in retrieving the current cricket matches”)
