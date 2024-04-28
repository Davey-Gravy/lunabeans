import requests

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

# Example usage
if __name__ == "__main__":
    query = 'python programming'  # Example search query
    max_results = 5  # Example maximum number of results
    search_results = search_videos(query, max_results)
    print(search_results)
