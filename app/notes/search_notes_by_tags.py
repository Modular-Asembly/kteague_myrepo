from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.modassembly.database.sql.get_sql_session import get_sql_session
from app.models.Note import Note
from app.models.Category import Category


def search_notes_by_tags(tag: str, db: Session) -> List[Note]:
    """
    1) Receives a tag.
    2) Searches the database for notes associated with the tag.
    3) Returns a list of matching notes.
    """
    stmt = (
        select(Note)
        .join(Category, Note.id == Category.id)
        .where(Category.name.__eq__(tag))
    )
    result = db.execute(stmt).scalars().all()
    return result
