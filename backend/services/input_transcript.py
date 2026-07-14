from youtube_transcript_api import YouTubeTranscriptApi
#fetch the transcript


def fetch_transcript(video_id,language):
    
    try:
        yt_api = YouTubeTranscriptApi()
        scripts =yt_api.fetch(video_id,languages=[language])
        transcript_text = " ".join(chunk.text for chunk in scripts)
        return  transcript_text
    except Exception as e:
        print('unable to load transcript \n error :', e )




