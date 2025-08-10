import argparse
from dto.message_data_transfer_object import (
  MessageDataTransferObject
)
from notifier.slack import SlackNotifier

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--token", required=False)
  parser.add_argument("--message", required=True)
  args = parser.parse_args()

  validatedData = MessageDataTransferObject(**args.__dict__)

  notifier = SlackNotifier()
  notifier.send(validatedData)
  print("Message sent successfully")
  
if __name__ == "__main__":
  main()