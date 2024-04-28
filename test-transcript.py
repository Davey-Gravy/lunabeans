from youtube_transcript_api import YouTubeTranscriptApi
from serach import search_videos

def getTranscript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        if transcript is None:
            return None
        else:
            returnText = []
            for item in transcript:
                returnText.append(item['text'])
            fullText = ' '.join(returnText)
            return fullText
    except Exception:
        return None

if __name__ == "__main__":
    search_term = 'python programming'
    results = search_videos(search_term, 5)
    for item in results['items']:
        itemKind = item['id']['kind']
        if itemKind == "youtube#video":
            print(item['id']['videoId'])
        elif itemKind == 'youtube#playlist':
            print(item['id']['playlistId'])
        
    videoID = 'TOe_TvQLAA'
    videoID1 = 'Wb3UrJjAac4'
    videoID2 = 'Wb3UrJjAac4'
    tr = getTranscript(videoID1)
    print(tr)

