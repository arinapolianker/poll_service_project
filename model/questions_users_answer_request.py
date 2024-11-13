from typing import Optional

from pydantic import BaseModel

from api.internalApi.user_service.model.user_response import UserResponse


class QuestionsUsersAnswerRequest(BaseModel):
    id: Optional[int] = None
    question_id: int
    user_id: int
    answer: str
