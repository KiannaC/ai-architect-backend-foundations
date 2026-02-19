from fastapi import FastAPI
from app.routes.agent import router as agent_router

app = FastAPI()

app.include_router(agent_router)

@app.get("/")
def read_root():
    return {"message": "AI Architect lab API is running!"}