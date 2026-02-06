from fastapi import APIRouter, Depends, HTTPException
from app.schemas.LLM_schema import AskLLMRequest, AskLLMResponse
from app.services.LLM.Cohere_service import CohereLLMService
from openai import RateLimitError
from app.api.deps import get_llm_service

router = APIRouter(prefix="/llm", tags=["LLM"])

@router.post("/ask", response_model=AskLLMResponse)
def ask_llm(
    request: AskLLMRequest,
    llm_service: CohereLLMService = Depends(get_llm_service),
):
    try:
        final_answer = llm_service.ask(request.prompt)
        return AskLLMResponse(answer=final_answer)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
