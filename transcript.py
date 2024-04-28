from youtube_transcript_api import YouTubeTranscriptApi
from search import search_videos, get_playlist_items

def getTranscriptFromVideo(video_id):
    '''
    Input:
        video_id: string
    Output:
        fullText: string containing video transcript, None if invalid or no captions
    '''
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        if transcript is None:
            return None
        else:
            returnText = [item['text'] for item in transcript]
            fullText = ' '.join(returnText)
            return fullText
    except Exception:
        return None
    
def getTranscriptFromPlaylist(playlist_id):
    '''
    Input:
        playlist_id: string
    Output:
        out: string containing all video transcripts
    '''
    videoIds = get_playlist_items(playlist_id)
    response = [getTranscriptFromVideo(vidId) for vidId in videoIds if getTranscriptFromVideo(vidId) is not None]
    out = ' '.join(response)
    return out

def searchQueryToTranscripts(search_term, max_results=2):
    '''
    Input: 
        search_term: string
    Output:
        transcripts: list of strings containing full transcripts of each video in search result
    '''
    results = search_videos(search_term, max_results)
    transcripts = []
    for item in results['items']:
        itemKind = item['id']['kind']
        if itemKind == "youtube#video":
            transcripts.append(getTranscriptFromVideo(item['id']['videoId']))
        elif itemKind == 'youtube#playlist':
            transcripts.append(getTranscriptFromPlaylist(item['id']['playlistId']))

    transcripts = [transcript for transcript in transcripts if transcript is not None]
    return transcripts

if __name__ == "__main__":
    search_term = 'dog eats bean burrito in one second'
    print(searchQueryToTranscripts(search_term,5))
    # results = search_videos(search_term, 5)
    # for item in results['items']:
    #     itemKind = item['id']['kind']
    #     if itemKind == "youtube#video":
    #         print(item['id']['videoId'])
    #     elif itemKind == 'youtube#playlist':
    #         print(item['id']['playlistId'])
        
    # videoID = 'TOe_TvQLAA'
    # videoID1 = 'PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3'
    # videoID2 = 'Wb3UrJjAac4'
    # tr1 = getTranscriptFromPlaylist(videoID1)
    # tr = getTranscriptFromVideo(videoID2)
    # # print(tr)
    # print(tr1)

