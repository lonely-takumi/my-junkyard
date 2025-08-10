from notifier.base import BaseNotifier
import requests
from utils.load_env import load_env
import os
from pydantic import BaseModel

class SlackNotifier(BaseNotifier):
  def __init__(self, validated_data: BaseModel):
    load_env()
    self.text = validated_data.text
    
  def send(self) -> None:
    data = {
      "text": self.text
    }
    result = requests.post(
      os.getenv("SLACK_WEBHOOK_URL"),
      json=data
    )
    print(f"Slack response: {result.status_code} - {result.text}")