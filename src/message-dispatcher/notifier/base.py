from abc import ABC, abstractmethod
from dto.message_data_transfer_object import (
  MessageDataTransferObject
)

class BaseNotifier(ABC):
  @abstractmethod
  def send(self, message: MessageDataTransferObject) -> None:
    pass