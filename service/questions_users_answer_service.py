from typing import Optional

from api.internalApi.user_service.model import user_response
from model.questions_users_answer import QuestionsUsersAnswer
from repository import questions_users_answer_repository


async def get_answer_by_id(answer_id: int) -> Optional[QuestionsUsersAnswer]:
    return await questions_users_answer_repository.get_answer_by_id(answer_id)


async def create_answer(answer: QuestionsUsersAnswer) -> int:
    question = await get_question_by_id(question_id)
    choices_mapping = {
        "a": question.a,
        "b": question.b,
        "c": question.c,
        "d": question.d
    }
    if selected_answer not in choices_mapping:
        raise ValueError("Invalid answer. Select 'a', 'b', 'c', or 'd'.")

    answer = choices_mapping[selected_answer]

    answer_exists = questions_users_answer_repository.get_answer_by_user_id_and_question_id(question_id, user_id)
    if user_response.UserResponse.registered is 0:
        if answer_exists:
            raise ValueError()
        return await questions_users_answer_repository.create_answer(question_id, user_id, selected_answer)


async def update_answer_by_id(answer_id: str, answer: QuestionsUsersAnswer):
    await questions_users_answer_repository.update_answer_by_id(answer_id, answer)


async def delete_answer_by_id(answer_id: int):
    if user_response.UserResponse.id is None:
        await questions_users_answer_repository.delete_answer_by_id(answer_id)
    await questions_users_answer_repository.delete_answer_by_id(answer_id)
