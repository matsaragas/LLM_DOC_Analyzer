from pydantic import BaseModel

class State(BaseModel):

    doc_name: str | None = None

