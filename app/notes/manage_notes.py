from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from typing import List, Optional
from pydantic import BaseModel
from app.notes.create_note import create_note
from app.notes.read_note import read_note
from app.notes.update_note import update_note
from app.notes.delete_note import delete_note
from app.notes.handle_file_attachment import handle_file_attachment
from sqlalchemy.orm import Session
from app.modassembly.database.sql.get_sql_session import get_sql_session

router = APIRouter()

class NoteCreate(BaseModel):
    user_id: int
    title: str
    content: str

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class NoteResponse(BaseModel):
    id: int
    user_id: int
    title: str
    content: str
    created_at: str
    updated_at: Optional[str] = None

@router.post("/notes/", response_model=NoteResponse)
def create_note_endpoint(note_data: NoteCreate, db: Session = next(get_sql_session())) -> NoteResponse:
    note = create_note(note_data.dict())
    return NoteResponse(**note)

@router.get("/notes/{note_id}", response_model=NoteResponse)
def read_note_endpoint(note_id: int, db: Session = next(get_sql_session())) -> NoteResponse:
    note = read_note(note_id)
    return NoteResponse(**note)

@router.put("/notes/{note_id}", response_model=NoteResponse)
def update_note_endpoint(note_id: int, note_data: NoteUpdate, db: Session = next(get_sql_session())) -> NoteResponse:
    note = update_note(db, note_id, note_data.dict(exclude_unset=True))
    return NoteResponse(**note)

@router.delete("/notes/{note_id}", response_model=dict)
def delete_note_endpoint(note_id: int, db: Session = next(get_sql_session())) -> dict:
    message = delete_note(note_id)
    return {"message": message}

@router.post("/notes/{note_id}/attachments/")
def handle_file_attachment_endpoint(note_id: int, file: UploadFile = File(...), db: Session = next(get_sql_session())) -> dict:
    file_data = file.file.read()
    file_metadata = handle_file_attachment(file_data, file.filename, note_id)
    return file_metadata
