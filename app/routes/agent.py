from fastapi import APIRouter
from app.models.schemas import ClientRequest

router = APIRouter()

@router.post("/agent")
def ai_agent(request: ClientRequest):
    response = f"Hello {request.name}, we received your inquiry about {request.service}. Our specialist will contact you shortly."

    return{
        "original_message": request.message,
        "agent_response": response
    }