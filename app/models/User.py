from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.modassembly.database.sql.get_sql_session import Base


class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    username: str = Column(String, unique=True, index=True, nullable=False)
    email: str = Column(String, unique=True, index=True, nullable=False)
    password_hash: str = Column(String, nullable=False)

    # Define relationships if needed, for example, with notes
    # notes = relationship("Note", back_populates="owner")
