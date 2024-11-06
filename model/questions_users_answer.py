from typing import Optional

from pydantic import BaseModel


class QuestionsUsersAnswer(BaseModel):
    id: Optional[int] = None
    question_id: int
    user_id: int
    answer: str

