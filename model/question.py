from typing import Optional

from pydantic import BaseModel


class Question(BaseModel):
    id: Optional[int] = None
    title: str
    a: str
    b: str
    c: str
    d: str



