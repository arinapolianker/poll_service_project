from typing import Optional

from pydantic import BaseModel


class QuestionsUsersAnswerRequest(BaseModel):
    id: Optional[int] = None
    question_id: int
    user_id: int
    answer: str
