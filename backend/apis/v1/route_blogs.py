from typing import List

from db.repository.blog import (
    create_new_blog,
    delete_blog_by_id,
    retrieve_blog,
    retrieve_blogs,
    update_blog_by_id,
)
from db.session import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.blog import CreateBlog, ShowBlog, UpdateBlog
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db, author_id=1)
    return blog


@router.get("/{id}", response_model=ShowBlog, status_code=status.HTTP_200_OK)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = retrieve_blog(id=id, db=db)
    if not blog:
        raise HTTPException(
            detail=f"Blog with id: {id} cannot be found.",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return blog


@router.get("", response_model=List[ShowBlog], status_code=status.HTTP_200_OK)
def get_blogs(db: Session = Depends(get_db)):
    blogs = retrieve_blogs(db=db)
    if not blogs:
        raise HTTPException(
            detail=f"No blogs can be found.",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return blogs


@router.put("/{id}", response_model=ShowBlog, status_code=status.HTTP_200_OK)
def update_blog(id: int, blog: UpdateBlog, db: Session = Depends(get_db)):
    blog = update_blog_by_id(id=id, blog=blog, db=db, author_id=1)
    if not blog:
        raise HTTPException(
            detail=f"Blog with id: {id} cannot be found.",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return blog


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = retrieve_blog(id=id, db=db)
    if not blog:
        raise HTTPException(
            detail=f"Blog with id: {id} cannot be found.",
            status_code=status.HTTP_404_NOT_FOUND,
        )

    return delete_blog_by_id(id=id, db=db)
