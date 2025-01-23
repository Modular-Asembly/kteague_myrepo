from sqlalchemy.orm import Session
from app.models.Note import Note
from app.modassembly.database.sql.get_sql_session import get_sql_session


def read_note(note_id: int) -> dict:
    with next(get_sql_session()) as db:  # type: Session
        note = db.query(Note).filter(Note.id == note_id).first()
        if note is None:
            raise ValueError(f"Note with ID {note_id} not found.")
        
        return {
            "id": note.id.__int__(),
            "user_id": note.user_id.__int__(),
            "title": note.title.__str__(),
            "content": note.content.__str__(),
            "created_at": note.created_at.isoformat(),
            "updated_at": note.updated_at.isoformat() if note.updated_at else None
        }
