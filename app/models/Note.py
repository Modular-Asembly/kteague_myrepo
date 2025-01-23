from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.modassembly.database.sql.get_sql_session import Base


class Note(Base):
    __tablename__ = "notes"

    id: int = Column(Integer, primary_key=True, index=True)
    user_id: int = Column(Integer, ForeignKey("users.id"), nullable=False)
    title: str = Column(String, index=True, nullable=False)
    content: str = Column(Text, nullable=False)
    created_at: DateTime = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: DateTime = Column(DateTime(timezone=True), onupdate=func.now(), nullable=False)

    owner = relationship("User", back_populates="notes")
