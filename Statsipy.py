import spotipy
import spotipy.oauth2 as oauth2
import sys
import json

credentials = oauth2.SpotifyClientCredentials(
        client_id="85dab73d4cfd4f14aac3eae199f9c38b",
        client_secret="4e81888314cd4043a87f173922473b55")
token = credentials.get_access_token()
sp = spotipy.Spotify(auth=token)
s = ["artist","album","playlist","track"]
j = 0

for i in s:
    j+=1
    print(j,i)

usr = int(input(">>> "))
usr-=1

print("Search for", s[usr])
q = input(">>> ")
look = sp.search(q, limit = 50,type = s[usr])

with open(q+".json","w") as outfile:
    json.dump(look, outfile)

c = 0

if usr == 0:
    for p in look["artists"]["items"]:
        c+=1
        print("[",c,"]")
        print("Artist: " + p["name"])
        print("-"* 10)
if usr == 1:
    for p in look["albums"]["items"]:
        c+=1
        print("[",c,"]")
        print("Artist: " + p["artists"][0]["name"])
        print("Album: " + p["name"])
        print("-"* 10)
if usr == 2:
    for p in look["playlists"]["items"]:
        c+=1
        print("[",c,"]")
        print("Name: " + p["name"])
        print("-"* 10)
if usr == 3:
    for p in look["tracks"]["items"]:
        c+=1
        print("[",c,"]")
        print("Artist: " + p["album"]["artists"][0]["name"])
        print("Track: " + p["name"])
        print("-"* 10)
    
