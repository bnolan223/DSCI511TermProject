import requests
import pandas as pd

# Define your API key (replace with your actual Last.fm API key)
API_KEY = 'YOUR_API_KEY'

artist_name = 'Bad Bunny'

# Function to get tracks of an artist from Last.fm
def get_artist_tracks(artist_name, api_key, page=1, limit=200):
    url = f'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={artist_name}&api_key={api_key}&format=json&page={page}&limit={limit}'
    response = requests.get(url)
    data = response.json()
    
    # Check for successful response
    if response.status_code == 200 and 'toptracks' in data:
        return data['toptracks']['track']
    else:
        print("Error retrieving data:", data.get('message', 'Unknown error'))
        return []

# Function to get additional artist information from Last.fm
def get_artist_info(artist_name, api_key):
    url = f'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist={artist_name}&api_key={api_key}&format=json'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200 and 'artist' in data:
        return data['artist']
    else:
        print("Error retrieving artist info:", data.get('message', 'Unknown error'))
        return {}

tracks = []
page = 1
while True:
    print(f"Fetching page {page}...")
    track_data = get_artist_tracks(artist_name, API_KEY, page=page)
    if not track_data:
        break
    tracks.extend(track_data)
    page += 1

# Get Bad Bunny's general information (listeners, biography, etc.)
artist_info = get_artist_info(artist_name, API_KEY)

track_list = []
for track in tracks:
    track_info = {
        'track_name': track['name'],
        'artist_name': track['artist']['name'],
        'playcount': track['playcount'],
        'listeners': track['listeners'],
        'url': track['url'],
        'image_url': track['image'][2]['#text'],  
    }
    track_list.append(track_info)

# Create a DataFrame from the track data
df_tracks = pd.DataFrame(track_list)

# Save to CSV
df_tracks.to_csv('bad_bunny_tracks.csv', index=False)

#if artist_info:
#    print("Artist Information:")
#    print(f"Name: {artist_info.get('name', 'N/A')}")
#    print(f"Listeners: {artist_info.get('stats', {}).get('listeners', 'N/A')}")
#    print(f"Playcount: {artist_info.get('stats', {}).get('playcount', 'N/A')}")
#    print(f"Biography: {artist_info.get('bio', {}).get('summary', 'N/A')}")
