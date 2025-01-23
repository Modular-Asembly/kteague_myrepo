from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.modassembly.database.sql.get_sql_session import Base


class Category(Base):
    __tablename__ = "categories"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, unique=True, index=True, nullable=False)

    # Define relationships if needed, e.g., notes = relationship("Note", back_populates="category")
