from sqlalchemy.orm import Session
from app.models.Category import Category
from app.modassembly.database.sql.get_sql_session import get_sql_session


def create_category(db: Session, name: str) -> Category:
    new_category = Category(name=name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category
