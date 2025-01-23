from sqlalchemy.orm import Session
from app.models.Category import Category
from app.modassembly.database.sql.get_sql_session import get_sql_session


def update_category(category_id: int, updated_data: dict) -> Category:
    with next(get_sql_session()) as session:  # type: Session
        category = session.query(Category).filter(Category.id == category_id).first()
        if not category:
            raise ValueError(f"Category with id {category_id} not found.")

        for key, value in updated_data.items():
            if hasattr(category, key):
                setattr(category, key, value)

        session.commit()
        session.refresh(category)
        return category
