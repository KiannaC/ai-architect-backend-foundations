from fastapi import FastAPI

app = FastAPI(
    title="AI Architect Lab API",
    description="Backend foundation for AI-based intelligent agents",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"status": "API is running successfully"}

@app.get("/agent-info")
def agent_info():
    return {
        "agent_name": "Intelligent Support Agent",
        "capabilities": [
            "Answer contextual questions",
            "Handle personalized conversations",
            "Integrate with AI models",
            "Scale to voice systems"
        ]
    }