from fastapi import FastAPI

from backend.routes import story_routes

app = FastAPI(title="Yugen Story Engine")
app.include_router(story_routes.router)
