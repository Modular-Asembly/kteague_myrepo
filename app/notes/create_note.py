from sqlalchemy.orm import Session
from app.models.Note import Note
from app.modassembly.database.sql.get_sql_session import get_sql_session
from typing import Dict


def create_note(note_data: Dict[str, str]) -> Note:
    with next(get_sql_session()) as db:  # type: Session
        note = Note(
            user_id=int(note_data["user_id"]),
            title=note_data["title"],
            content=note_data["content"]
        )
        db.add(note)
        db.commit()
        db.refresh(note)
        return note
