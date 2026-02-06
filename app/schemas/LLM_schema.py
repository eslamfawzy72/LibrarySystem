from pydantic import BaseModel

class AskLLMRequest(BaseModel):
    prompt: str

class AskLLMResponse(BaseModel):
    answer: str
