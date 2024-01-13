# tests/logic_tests.py
import unittest
from logic.compute_sentiments import ComputeSentiments

class ComputeSentimentsTest(unittest.TestCase):

    def test_global_average_sentiments_when_no_sentences_should_raise_exception(self):
        sentences = []

        with self.assertRaises(Exception) as context:
            ComputeSentiments(sentences=sentences).global_average_sentiments()

        self.assertEqual(str(context.exception), "you must provide at least one sentence")

    def test_global_average_sentiments_when_only_one_sentence_should_return_correct_average(self):
        sentence = "I'm very happy to see you here"
        compute_sentiment = ComputeSentiments(sentences=sentence)
        expected_average = compute_sentiment.classifier(sentence)

        result = ComputeSentiments(sentences=sentence).global_average_sentiments()

        self.assertEqual(result, expected_average)



if __name__ == '__main__':
    unittest.main()
