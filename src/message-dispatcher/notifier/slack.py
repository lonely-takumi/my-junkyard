from dto.message_data_transfer_object import (
  MessageDataTransferObject
)
from .base import BaseNotifier
import requests
from utils.load_env import load_env
import os

class SlackNotifier(BaseNotifier):
  def __init__(self):
    load_env()
    
  def send(self, message: MessageDataTransferObject) -> None:
    data = {
      "text": message.message
    }
    result = requests.post(
      os.getenv("SLACK_WEBHOOK_URL"),
      json=data
    )
    print(f"Slack response: {result.status_code} - {result.text}")