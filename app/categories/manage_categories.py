from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from app.modassembly.database.sql.get_sql_session import get_sql_session
from app.models.Category import Category
from app.categories.create_category import create_category
from app.categories.read_categories import read_categories
from app.categories.update_category import update_category
from app.categories.delete_category import delete_category

router = APIRouter()

class CategoryCreate(BaseModel):
    name: str

class CategoryUpdate(BaseModel):
    name: str

class CategoryResponse(BaseModel):
    id: int
    name: str

@router.post("/categories/", response_model=CategoryResponse)
def create_category_endpoint(category: CategoryCreate, db: Session = Depends(get_sql_session)) -> CategoryResponse:
    """
    Create a new category.
    """
    new_category = create_category(db, category.name)
    return CategoryResponse(id=new_category.id.__int__(), name=new_category.name.__str__())

@router.get("/categories/", response_model=List[CategoryResponse])
def read_categories_endpoint(db: Session = Depends(get_sql_session)) -> List[CategoryResponse]:
    """
    Retrieve all categories.
    """
    categories = read_categories(db)
    return [CategoryResponse(id=cat.id.__int__(), name=cat.name.__str__()) for cat in categories]

@router.put("/categories/{category_id}", response_model=CategoryResponse)
def update_category_endpoint(category_id: int, category: CategoryUpdate, db: Session = Depends(get_sql_session)) -> CategoryResponse:
    """
    Update an existing category.
    """
    updated_category = update_category(category_id, category.dict())
    return CategoryResponse(id=updated_category.id.__int__(), name=updated_category.name.__str__())

@router.delete("/categories/{category_id}", response_model=str)
def delete_category_endpoint(category_id: int, db: Session = Depends(get_sql_session)) -> str:
    """
    Delete a category.
    """
    return delete_category(category_id)
