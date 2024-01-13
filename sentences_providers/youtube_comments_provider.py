import sys
import os

from decouple import config, UndefinedValueError
from googleapiclient.discovery import build
from sentences_providers.sentences_provider import SentencesProviderInterface

class YoutubeCommentsProvider(SentencesProviderInterface):

    def __init__(self, video_id: str) -> None:
        super().__init__()
        self.video_id = video_id
        try:
            self.api_key = config('YOUTUBE_API_KEY')
        except UndefinedValueError:
            self.api_key = None
    
    def get_sentences(self, max: int) -> list[str]:
        return self.get_comments_of_video(max)

    def get_comments_of_video(self, max_results: int = 100) -> list[str]:
        if self.api_key == None:
            raise Exception("No Youtube API Key set in .env - See .env.template to set needed secrets")
        
        youtube_service = build('youtube', 'v3', developerKey=self.api_key)
        video_id = self.video_id
        comments = []

        request = youtube_service.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            order='relevance',
            maxResults=min(100, max_results)
        )

        while request:
            response = request.execute()

            for comment in response.get("items", []):
                comment_text = comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
                
                comments.append(comment_text[ : int(config("SENTENCE_TRUNCATION_LENGTH")) ])

            max_results -= min(100, max_results)

            nextPageToken = response.get("nextPageToken")
            if nextPageToken and max_results > 0:
                request = youtube_service.commentThreads().list(
                    part="snippet",
                    videoId=video_id,
                    textFormat="plainText",
                    order='relevance',
                    maxResults=min(100, max_results),
                    pageToken=nextPageToken
                )
            else:
                break

        return comments



