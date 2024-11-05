from typing import Optional

from pydantic import BaseModel


class Question(BaseModel):
    question_id: Optional[int] = None
    title: str
    first_answer: str
    second_answer: str
    third_answer: str
    fourth_answer: str
