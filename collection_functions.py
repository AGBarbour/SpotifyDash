import requests
import json

access_token = ""

# time_range can be entered as "short", "medium", or "long"
def artist_search(time_range, access_token):
    
    artists = []
    
    #   Spotify API endpoint which returns users top artist for the specified time range
    endpoint = f"https://api.spotify.com/v1/me/top/artists?time_range={time_range}_term&limit=50"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(endpoint, headers=headers).json()
    
    items = response["items"]

    for item in items:

        genres = item["genres"]
        artist = item["name"]
        images = item["images"]
        artist_id = item["id"]
        popularity = item["popularity"]
        artist_url = item["external_urls"]["spotify"]
        followers = item["followers"]["total"]

        artists.append({
            "genres": genres,
            "artist": artist,
            "id": artist_id,
            "images": images,
            "popularity": popularity,
            "artist_url": artist_url,
            "followers": followers
        })

    return artists

# time_range can be entered as "short", "medium", or "long"
def track_search(time_range, access_token):
    
    tracks = []

    #   Spotify API endpoint which returns users top tracks for the specified time range
    endpoint = f"https://api.spotify.com/v1/me/top/tracks?time_range={time_range}_term&limit=50"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(endpoint, headers=headers).json()

    items = response["items"]

    for item in items:

        song = item["name"]
        artists = item["artists"][0]["name"]
        duration_ms = item["duration_ms"]
        song_id = item["id"]
        popularity = item["popularity"]
        preview_url = item["preview_url"]
        web_player_url = item["external_urls"]["spotify"]
        release_date = item["album"]["release_date"]
        release_date_precision = item["album"]["release_date_precision"]

        tracks.append({
            "song": song,
            "artists": artists,
            "id": song_id,
            "duration_ms": duration_ms,
            "popularity": popularity,
            "preview_url": preview_url,
            "web_player_url": web_player_url,
            "release_date": release_date,
            "release_date_precision": release_date_precision

        })
        
    return tracks


