from youtube_transcript_api import YouTubeTranscriptApi

def getTranscript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return transcript


if __name__ == "__main__":
    video_id = 'haT7uxmIFA8'
    transcript = getTranscript(video_id)
    for item in transcript:
        print(item['text'])
