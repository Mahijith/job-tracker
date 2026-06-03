from fastapi import FastAPI

app = FastAPI(
    title="Job Tracker API",
    description="Track your job applications",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}