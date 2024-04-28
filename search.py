import requests
import json

# Set your API key
API_KEY = 'AIzaSyD3n85SEaOKpRCqEJcguQjC2jMowXvESyk'

# Function to search for videos on YouTube
def search_videos(query, max_results=10):
    base_url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part': 'snippet',
        'q': query,
        'maxResults': max_results,
        'key': API_KEY
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def get_playlist_items(playlist_id, max_results=10):
    base_url = 'https://www.googleapis.com/youtube/v3/playlistItems'
    params = {
        'part': 'snippet',
        'maxResults': max_results,
        'key': API_KEY,
        'playlistId': playlist_id
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    
    # Extract the video IDs from the search results
    video_ids = [item['snippet']['resourceId']['videoId'] for item in data['items']]
    
    return video_ids

# Example usage
if __name__ == "__main__":
    query = 'python programming'  # Example search query
    max_results = 5  # Example maximum number of results
    search_results = search_videos(query, max_results)
    with open('test.json', 'w') as f:
        json.dump(search_results, f, indent=4)
    # print(search_results)
    pli = get_playlist_items('PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3')
    print(pli)
