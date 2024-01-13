# logic/logic.py
from transformers import pipeline
import json

class ComputeSentiments:

    def __init__(self, sentences : list[str]) -> None:
        self.classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
        self.sentences = sentences

    def global_average_sentiments(self) -> str:
        """
        Compute average sentiments of sentence on 28 labels : 
            - disappointment
            - sadness
            - annoyance
            - neutral
            - disapproval
            - realization
            - nervousness
            - approval
            - joy
            - anger
            - embarrassment
            - caring
            - remorse
            - disgust
            - grief
            - confusion
            - relief
            - desire
            - admiration
            - optimism
            - fear
            - love
            - excitement
            - curiosity
            - amusement
            - surprise
            - gratitude
            - pride

        Returns:
            str - JSON representation of {sentiment_label: average_score}
        
        """
        if len(self.sentences) == 0:
            raise Exception("you must provide at least one sentence")
    
        try:
            sentiments_of_sentences = self.classifier(self.sentences)
        except RuntimeError:
            raise Exception("error batch size: too many tokens to compute")
        
        complete_labels = [label for label in sentiments_of_sentences[0][0]['label'] if len(label) > 1]

        totals = {label: 0.0 for label in complete_labels}

        num_sentences = len(sentiments_of_sentences)
        for sentence_scores in sentiments_of_sentences:
            for sentiment_score in sentence_scores:
                label = sentiment_score['label']
                score = sentiment_score['score']
                
                if label in totals:
                    totals[label] += score
                else:
                    totals[label] = score

        labels_averages = {label: total / num_sentences for label, total in totals.items()}
        sorted_labels_averages = dict(sorted(labels_averages.items(), key=lambda item: item[1], reverse=True))
        averages_json = {"averages": sorted_labels_averages}
        json_result = json.dumps(averages_json, indent=2)
        return json_result