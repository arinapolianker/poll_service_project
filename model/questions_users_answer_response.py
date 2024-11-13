from typing import Optional

from pydantic import BaseModel

from model.question import Question


class QuestionsUsersAnswerResponse(BaseModel):
    id: Optional[int] = None
    user_id: int
    question_id: int
    question_title: str
    answer: str
