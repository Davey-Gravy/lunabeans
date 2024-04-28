from youtube_transcript_api import YouTubeTranscriptApi
from search import search_videos, get_playlist_items, get_video_info

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
    response = [getTranscriptFromVideo(videoId) for videoId in videoIds if getTranscriptFromVideo(videoId) is not None]
    out = ' '.join(response)
    return out

def searchQueryToData(search_term, max_results=2, ignorePlaylist=True):
    '''
    Input: 
        search_term: string
    Output:
        videodata: dictionary mapping videoId to tuple of video transcript and video metadata
            metadata: views_count, likes_count    
    '''
    results = search_videos(search_term, max_results)
    videodata = {}
    for item in results['items']:
        itemKind = item['id']['kind']
        if itemKind == "youtube#video":
            videoId = item['id']['videoId']
            transcript = getTranscriptFromVideo(videoId)
            video_metadata = get_video_info(videoId)
            videodata[videoId] = (transcript, video_metadata)
        elif itemKind == 'youtube#playlist':
            if ignorePlaylist:
                pass
            # else:
            #     transcripts.append(getTranscriptFromPlaylist(item['id']['playlistId']))

    # transcripts = [transcript for transcript in transcripts if transcript is not None]
    # return transcripts
    return videodata

if __name__ == "__main__":
    search_term = 'dog eats bean burrito in one second'
    data = searchQueryToData(search_term,5)

    for (key, item) in data.items():
        print(key + ": " + str(item[0]))
    # print(getTranscriptFromPlaylist('PLEG35I51CH7W6bOW3UbkjHRSQfdSk3TRh'))

    # videoID = 'TOe_TvQLAA'
    # videoID1 = 'PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3'
    # videoID2 = 'Wb3UrJjAac4'
    # tr1 = getTranscriptFromPlaylist(videoID1)
    # tr = getTranscriptFromVideo(videoID2)
    # # print(tr)
    # print(tr1)

