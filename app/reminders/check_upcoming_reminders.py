from datetime import datetime, timedelta
from typing import List
from sqlalchemy.orm import Session
from app.modassembly.database.sql.get_sql_session import get_sql_session
from app.models.Note import Note


def check_upcoming_reminders(session: Session = next(get_sql_session())) -> List[Note]:
    """
    Queries the database for notes with reminders set for the near future.
    Returns a list of notes with upcoming reminders.
    """
    # Define the time window for upcoming reminders (e.g., next 24 hours)
    time_window = datetime.utcnow() + timedelta(hours=24)

    # Query the database for notes with reminders set within the time window
    upcoming_reminders = session.query(Note).filter(Note.reminder_time <= time_window).all()

    return upcoming_reminders
