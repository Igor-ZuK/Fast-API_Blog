from typing import List
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

import database
import schemas
import oauth
from repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blog']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(request, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(database.get_db)):
    return blog.delete(id, db)


@router.get('/', response_model=List[schemas.ShowBlog])
def get_all(
        db: Session = Depends(database.get_db),
        get_current_user: schemas.User = Depends(oauth.get_current_user)
):
    return blog.get_all(db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def get_blog(id: int, db: Session = Depends(database.get_db)):
    return blog.retrieve(id, db)
