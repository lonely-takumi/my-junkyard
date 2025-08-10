from abc import ABC, abstractmethod

class BaseNotifier(ABC):
  @abstractmethod
  def send(self) -> None:
    pass