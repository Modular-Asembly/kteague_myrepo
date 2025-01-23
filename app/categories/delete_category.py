from sqlalchemy.orm import Session
from app.models.Category import Category
from app.modassembly.database.sql.get_sql_session import get_sql_session


def delete_category(category_id: int) -> str:
    with next(get_sql_session()) as session:  # type: Session
        category = session.query(Category).filter(Category.id == category_id).first()
        if category:
            session.delete(category)
            session.commit()
            return f"Category with ID {category_id} has been successfully deleted."
        else:
            return f"Category with ID {category_id} does not exist."
