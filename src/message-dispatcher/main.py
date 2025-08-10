from dto.dto_factory import DataTransferObjectFactory
from notifier.notifier_factory import NotifierFactory

def main():
  appName = "slack"

  dataModel = DataTransferObjectFactory.create_dto(appName)
  validatedData = dataModel(**
    {
      "text": "test"
    }
  )
  
  variables = {
    "validated": validatedData,
    "appName": appName
  }

  notifier = NotifierFactory.get_notifier(**variables)
  notifier.send()
  print("Message sent successfully")
  
if __name__ == "__main__":
  main()