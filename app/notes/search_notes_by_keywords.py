from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.modassembly.database.sql.get_sql_session import get_sql_session
from app.models.Note import Note


def search_notes_by_keywords(db: Session, keyword: str) -> List[Note]:
    """
    Searches the database for notes containing the keyword in the title or content.
    
    :param db: Database session.
    :param keyword: Keyword to search for in notes.
    :return: List of matching notes.
    """
    keyword_pattern = f"%{keyword}%"
    notes = db.query(Note).filter(
        or_(
            Note.title.__str__().ilike(keyword_pattern),
            Note.content.__str__().ilike(keyword_pattern)
        )
    ).all()
    return notes
