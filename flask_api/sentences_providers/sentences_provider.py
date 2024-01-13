from abc import abstractmethod

class SentencesProviderInterface:
  @abstractmethod
  def get_sentences() -> list[str]:
     """
     Implement this method and return the sentences as you wish, from a file, 
     from Youtube comments, from Twitter comments, from RottenTomatoes, AlloCiné, etc ...

     You just have to provide sentences into a list of str.
     """
     pass