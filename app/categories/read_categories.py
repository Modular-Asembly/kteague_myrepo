from typing import List
from sqlalchemy.orm import Session
from app.modassembly.database.sql.get_sql_session import get_sql_session
from app.models.Category import Category


def read_categories(db: Session) -> List[Category]:
    categories = db.query(Category).all()
    return categories


# Example usage
# with get_sql_session() as session:
#     categories = read_categories(session)
#     for category in categories:
#         print(category.id.__str__(), category.name.__str__())
