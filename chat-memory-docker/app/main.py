from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from .db import SessionLocal, engine, Base
from .models import Message
from .openai_client import get_response

# Initialize database
Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def read_root(request: Request):
    db = SessionLocal()
    messages = db.query(Message).order_by(Message.timestamp.desc()).all()
    db.close()
    return templates.TemplateResponse("index.html", {"request": request, "messages": messages})

@app.post("/submit")
def submit(request: Request, prompt: str = Form(...)):
    answer = get_response(prompt)
    db = SessionLocal()
    msg = Message(prompt=prompt, response=answer)
    db.add(msg)
    db.commit()
    db.close()
    return RedirectResponse("/", status_code=303)
