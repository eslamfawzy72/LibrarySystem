from app.schemas.LLM_schema import AskLLMResponse

class CohereLLMService:
    def __init__(self, llm_client):
        self.llm_client = llm_client

    def ask(self, prompt: str) -> str:
        result: AskLLMResponse = self.llm_client.ask(prompt)
        return result.answer
