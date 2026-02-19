from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
import models
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Pydantic Schemas
class CourseCreate(BaseModel):
    name: str
    description: str
    price: float
    is_active: bool = True

class MessageCreate(BaseModel):
    text: str
    is_active: bool = True

class MessageUpdate(BaseModel):
    text: str
    is_active: bool = True

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/me")
def read_me():
    return "Hello World"

@app.post("/courses")
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = models.Course(name=course.name, description=course.description, price=course.price, is_active=course.is_active)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@app.post("/messages")
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    db_message = models.Message(text=message.text, is_active=message.is_active)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

@app.put("/messages/{message_id}")
def update_message(message_id: int, message: MessageUpdate, db: Session = Depends(get_db)):
    db_message = db.query(models.Message).filter(models.Message.id == message_id).first()
    if not db_message:
        raise HTTPException(status_code=404, detail="Message not found")
    db_message.text = message.text
    db_message.is_active = message.is_active
    db.commit()
    db.refresh(db_message)
    return db_message

@app.delete("/messages/{message_id}")
def delete_message(message_id: int, db: Session = Depends(get_db)):
    db_message = db.query(models.Message).filter(models.Message.id == message_id).first()
    if not db_message:
        raise HTTPException(status_code=404, detail="Message not found")
    db.delete(db_message)
    db.commit()
    return {"message_id": message_id, "message": "Message deleted"}