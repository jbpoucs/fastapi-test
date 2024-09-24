from datetime import datetime
from typing import Optional

from pydantic import BaseModel, root_validator


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if "title" in values:
            slug = values["title"].replace(" ", "_").lower()
            values["slug"] = slug
            return values


class UpdateBlog(CreateBlog):
    pass


class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
