
playlist = {
    "title": "patagonia bus",
    "created_by": "Colt Steele",
    "songs": [
        {"title": "Turn it off", "artist": ["Culture Abuse"], "Album": "Peach", "duration": 2.5},
        {"title": "Nights Off", "artist": ["Sirusom", "kitty"], "Album": "Mosaik", "duration": 5.25},
        {"title": "meow", "artist": ["garfielsd"], "Album": "Kitty2", "duration": 2.0}
    ]
}

print(playlist)

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']

print(total_length)
