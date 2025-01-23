from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Union
from pydantic import BaseModel
from app.modassembly.database.sql.get_sql_session import get_sql_session
from app.notes.search_notes_by_keywords import search_notes_by_keywords
from app.notes.search_notes_by_tags import search_notes_by_tags
from app.models.Note import Note

router = APIRouter()

class NoteResponse(BaseModel):
    id: int
    user_id: int
    title: str
    content: str
    created_at: str
    updated_at: Union[str, None]

@router.get("/search_notes", response_model=List[NoteResponse])
def search_notes(
    keyword: Union[str, None] = None,
    tag: Union[str, None] = None,
    db: Session = Depends(get_sql_session)
) -> List[NoteResponse]:
    """
    Search notes by keyword or tag.

    - **keyword**: Optional keyword to search in note titles and content.
    - **tag**: Optional tag to search for associated notes.

    Returns a list of notes matching the search criteria.
    """
    if keyword:
        notes = search_notes_by_keywords(keyword, db)
    elif tag:
        notes = search_notes_by_tags(tag, db)
    else:
        raise HTTPException(status_code=400, detail="Either keyword or tag must be provided.")

    return [
        NoteResponse(
            id=note.id.__int__(),
            user_id=note.user_id.__int__(),
            title=note.title.__str__(),
            content=note.content.__str__(),
            created_at=note.created_at.isoformat(),
            updated_at=note.updated_at.isoformat() if note.updated_at else None
        )
        for note in notes
    ]
