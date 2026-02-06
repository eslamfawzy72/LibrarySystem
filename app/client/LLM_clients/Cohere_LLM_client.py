import cohere
from app.core.config import get_settings
from app.schemas.LLM_schema import AskLLMResponse

class CohereLLMClient:
    def __init__(self):
        settings = get_settings()
        self.client = cohere.Client(settings.COHERE_API_KEY)

    def ask(self, prompt: str) -> AskLLMResponse:
        response = self.client.chat(
            model="command-a-03-2025",
            temperature=0.5,
            message=prompt,
            preamble=(
                "You are an API. "
                "Return ONLY valid JSON in the form: "
                "{ \"answer\": string }"
            ),
        )

        
        return AskLLMResponse(answer=response.text)
