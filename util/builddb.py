from os import listdir
import json

photo_path = "../photos"
out_path = "../data/photos.json"

photos = listdir(photo_path)

photo_list_json = json.dumps(photos)

with open(out_path, 'w') as photo_db:
	photo_db.write(photo_list_json)

