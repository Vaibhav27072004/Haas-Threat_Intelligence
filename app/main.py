from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from app.database import Base, engine
from app.routes import user_routes, honeypot_routes

app = FastAPI()
Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app.include_router(user_routes.router, prefix="/api", tags=["users"])
app.include_router(honeypot_routes.router, prefix="/api", tags=["honeypot"])

@app.get("/")
def root():
    return {"message": "Welcome to Honeypot-as-a-Service!"}

@app.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
