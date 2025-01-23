from fastapi import APIRouter, HTTPException
from typing import List
from app.reminders.check_upcoming_reminders import check_upcoming_reminders
from app.reminders.send_email_notifications import send_email_notifications
from app.models.Note import Note
from app.modassembly.database.sql.get_sql_session import get_sql_session
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/reminders/schedule", response_model=List[dict])
async def handle_scheduled_reminders() -> List[dict]:
    """
    Endpoint to handle scheduled reminders.
    
    - Checks for notes with upcoming reminders.
    - Sends email notifications to users.
    
    Returns a list of notes for which reminders were sent.
    """
    with next(get_sql_session()) as db:  # type: Session
        upcoming_notes: List[Note] = check_upcoming_reminders(db)
        
        if not upcoming_notes:
            raise HTTPException(status_code=404, detail="No upcoming reminders found.")
        
        send_email_notifications(upcoming_notes, db)
        
        return [
            {
                "id": note.id.__int__(),
                "user_id": note.user_id.__int__(),
                "title": note.title.__str__(),
                "content": note.content.__str__(),
                "reminder_time": note.reminder_time.isoformat() if note.reminder_time else None
            }
            for note in upcoming_notes
        ]
