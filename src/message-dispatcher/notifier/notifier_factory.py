from notifier.slack import SlackNotifier
from pydantic import BaseModel

class NotifierFactory:

  @staticmethod
  def get_notifier(**kwargs):
    app_name = kwargs.get("appName")
    validated_data = kwargs.get("validated")

    if app_name == "slack":
      return SlackNotifier(validated_data)
    raise ImportError(f"Notifier for '{app_name}' is not supported.")