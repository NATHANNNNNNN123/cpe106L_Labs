from pymongo import MongoClient
import pprint
import re

client = MongoClient("mongodb://localhost:27017/")
db = client["chinook"]

albums_collection = db["albums"]
tracks_collection = db["tracks"]
artists_collection = db["artists"]

for artist in artists_collection.find():
    print(f"Artist: {artist['Name']}")
    albums = albums_collection.find({"ArtistId": artist["ArtistId"]})
    for album in albums:
        print(f"  Album: {album['Title']}")
        tracks = tracks_collection.find({"AlbumId": album["AlbumId"]})
        for track in tracks:
            print(f"      - {track['Name']}")