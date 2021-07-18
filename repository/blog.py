from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import models
import schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def retrieve(id: int, db: Session):
    blog = db.query(models.Blog).filter_by(id=id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    return blog


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter_by(id=id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog was not found")
    blog.update(request)
    db.commit()
    return "Updated"


def delete(id: int, db: Session):
    db.query(models.Blog).filter_by(id=id).delete()
    db.commit()

    return {'data': 'done'}
