from service.service import ServiceInterface
from logic.compute_sentiments import ComputeSentiments
from logic.compute_wordcloud import ComputeWordCloud
from sentences_providers.youtube_comments_provider import YoutubeCommentsProvider
import json

class ServiceImpl(ServiceInterface):

    def execute(self, options: {}) -> str:
        """
        Params:
            options: dict - you must set a "video_id" key with his value
        """
        video_id = options["video_id"]
        if video_id == None:
            raise Exception("options 'video_id' is missing")
        
        comments = YoutubeCommentsProvider(video_id).get_sentences(100)
    
        averages = ComputeSentiments(sentences=comments).global_average_sentiments()
        wordcloud = ComputeWordCloud(sentences=comments).get_word_cloud(20)

        merged_results = {
            "average": json.loads(averages),
            "wordcloud": json.loads(wordcloud)
        }

        return merged_results