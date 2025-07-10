from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from .db import SessionLocal, engine, Base, init_settings_table, get_setting, set_setting
from .models import Message
from .openai_client import get_response, list_models

# Initialize database
Base.metadata.create_all(bind=engine)

init_settings_table()

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def read_root(request: Request):
    db = SessionLocal()
    messages = db.query(Message).order_by(Message.timestamp.desc()).all()
    db.close()
    models = list_models()
    last_model = get_setting("last_model") or "gpt-4o"
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "messages": messages,
            "models": models,
            "last_model": last_model
        }
    )

@app.post("/submit")
def submit(request: Request, prompt: str = Form(...), model: str = Form("gpt-4o")):
    answer = get_response(prompt, model)
    db = SessionLocal()
    msg = Message(prompt=prompt, response=answer)
    db.add(msg)
    db.commit()
    db.close()
    set_setting("last_model", model)
    return RedirectResponse("/", status_code=303)

@app.get("/models")
def get_models():
    return {"models": list_models()}
