import os
from typing import List
from app.modassembly.email.get_email_client import get_email_client, EmailClient
from app.models.User import User
from app.models.Note import Note
from sqlalchemy.orm import Session


def send_email_notifications(notes: List[Note], db: Session) -> None:
    smtp_server = os.environ["SMTP_SERVER"]
    smtp_port = int(os.environ["SMTP_PORT"])
    smtp_username = os.environ["SMTP_USERNAME"]
    smtp_password = os.environ["SMTP_PASSWORD"]

    email_client: EmailClient = get_email_client(smtp_server, smtp_port, smtp_username, smtp_password)

    for note in notes:
        user: User = db.query(User).filter(User.id == note.user_id).first()
        if user:
            subject = f"Reminder: {note.title.__str__()}"
            body = f"Dear {user.username.__str__()},\n\nThis is a reminder for your note titled '{note.title.__str__()}'.\n\nContent:\n{note.content.__str__()}\n\nBest regards,\nYour Note-Taking App"
            email_client.send_email(user.email.__str__(), subject, body)
