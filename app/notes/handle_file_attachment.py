from typing import Dict
from sqlalchemy.orm import Session
from google.cloud import storage
from app.modassembly.storage.get_gcs_bucket import get_gcp_bucket
from app.modassembly.database.sql.get_sql_session import get_sql_session
from app.models.FileAttachment import FileAttachment


def handle_file_attachment(file_data: bytes, file_name: str, note_id: int) -> Dict[str, str]:
    # Upload the file to Cloud Storage
    bucket = get_gcp_bucket()
    blob = bucket.blob(file_name)
    blob.upload_from_string(file_data)

    # Store file metadata in the database
    with get_sql_session() as session:
        file_attachment = FileAttachment(
            note_id=note_id,
            file_path=blob.public_url
        )
        session.add(file_attachment)
        session.commit()
        session.refresh(file_attachment)

    # Return the file metadata
    return {
        "id": file_attachment.id.__str__(),
        "note_id": file_attachment.note_id.__str__(),
        "file_path": file_attachment.file_path.__str__(),
        "uploaded_at": file_attachment.uploaded_at.isoformat()
    }
