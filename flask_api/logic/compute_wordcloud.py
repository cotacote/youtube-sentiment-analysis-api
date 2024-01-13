from wordcloud import WordCloud
import json

class ComputeWordCloud:

    def __init__(self, sentences: list[str]) -> None:
        self.sentences = sentences
    
    def get_word_cloud(self, max_words: int = 20) -> str:
        """
        Compute word cloud of self.sentences
        Returns:
            str - JSON representation of {word: occurence_count}
        """
        if len(self.sentences) == 0:
            raise Exception("you must provide at least one sentence to compute word cloud")
        
        text = " ".join(self.sentences)
        wordcloud = WordCloud(max_words=max_words, min_word_length=3).generate(text)

        wordcloud_data = {"words": []}

        for word, count in wordcloud.words_.items():
            wordcloud_data["words"].append({"word": word, "frequency": count})

        return json.dumps(wordcloud_data, indent=2)
        


if __name__ == '__main__':
    pass