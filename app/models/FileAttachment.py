from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.modassembly.database.sql.get_sql_session import Base


class FileAttachment(Base):
    __tablename__ = "file_attachments"

    id: int = Column(Integer, primary_key=True, index=True)
    note_id: int = Column(Integer, ForeignKey("notes.id"), nullable=False)
    file_path: str = Column(String, nullable=False)
    uploaded_at: DateTime = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    note = relationship("Note", back_populates="attachments")
