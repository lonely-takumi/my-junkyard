from dto.slack_data_transfer_object import SlackDataTransferObject

class DataTransferObjectFactory:
  @staticmethod
  def create_dto(appName: str):
    if appName == "slack":
      return SlackDataTransferObject