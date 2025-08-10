from pydantic import BaseModel

class MessageDataTransferObject(BaseModel):
    message: str
    token: str | None = None
