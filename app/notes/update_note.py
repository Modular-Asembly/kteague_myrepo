from typing import Dict, Any
from sqlalchemy.orm import Session
from app.modassembly.database.sql.get_sql_session import get_sql_session
from app.models.Note import Note


def update_note(
    db: Session, note_id: int, updated_data: Dict[str, Any]
) -> Note:
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise ValueError(f"Note with id {note_id} not found.")

    for key, value in updated_data.items():
        if hasattr(note, key):
            setattr(note, key, value)

    db.commit()
    db.refresh(note)
    return note
