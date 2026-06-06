from fastapi import FastAPI
from app.routers import jobs

app = FastAPI(
    title="Job Tracker API",
    description="Track your job applications",
    version="0.1.0"
)

app.include_router(jobs.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}