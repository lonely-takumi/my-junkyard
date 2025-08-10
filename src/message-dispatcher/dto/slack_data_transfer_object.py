from pydantic import BaseModel

class SlackDataTransferObject(BaseModel):
    text: str
