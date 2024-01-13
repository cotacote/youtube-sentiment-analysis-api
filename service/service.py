from abc import abstractmethod

class ServiceInterface:
  @abstractmethod
  def execute(options: dict = {}) -> any:
     pass
