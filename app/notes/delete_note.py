from sqlalchemy.orm import Session
from app.models.Note import Note
from app.modassembly.database.sql.get_sql_session import get_sql_session
from typing import Iterator


def delete_note(note_id: int) -> str:
    session_iterator: Iterator[Session] = get_sql_session()
    session: Session = next(session_iterator)
    try:
        note: Note = session.query(Note).filter(Note.id == note_id).first()
        if note is None:
            raise ValueError(f"Note with ID {note_id} does not exist.")
        
        session.delete(note)
        session.commit()
        
        return f"Note with ID {note_id} has been successfully deleted."
    finally:
        session.close()
