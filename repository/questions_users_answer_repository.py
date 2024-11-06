from typing import Optional

from model.questions_users_answer import QuestionsUsersAnswer
from repository.database import database
from repository.question_repository import get_question_by_id

TABLE_NAME = "questions_users_answer"


async def get_answer_by_id(answer_id: int) -> Optional[QuestionsUsersAnswer]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id=:answer_id"
    result = await database.fetch_one(query, values={"answer_id": answer_id})
    if result:
        return QuestionsUsersAnswer(**result)
    else:
        return None


async def get_answer_by_user_id_and_question_id(question_id: int, user_id) -> Optional[QuestionsUsersAnswer]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id=:question_id AND user_id=:user_id"
    result = await database.fetch_one(query, values={"question_id": question_id, "user_id": user_id})
    if result:
        return QuestionsUsersAnswer(**result)
    else:
        return None


async def create_answer(answer: QuestionsUsersAnswer) -> int:
    # question = await get_question_by_id(question_id)
    # choices_mapping = {
    #     "a": question.a,
    #     "b": question.b,
    #     "c": question.c,
    #     "d": question.d
    # }
    # if selected_answer not in choices_mapping:
    #     raise ValueError("Invalid answer. Select 'a', 'b', 'c', or 'd'.")
    #
    # answer = choices_mapping[selected_answer]
    query = f"""
        INSERT INTO {TABLE_NAME} (question_id, user_id, answer)
        VALUES (:question_id, :user_id, :answer)
    """
    values = {
        "question_id": answer.question_id,
        "user_id": answer.user_id,
        "answer": answer.answer
    }

    async with database.transaction():
        await database.execute(query, values)
        last_record_id = await database.fetch_one("SELECT LAST_INSERT_ID()")
    return last_record_id[0] if last_record_id else None


async def update_answer_by_id(answer_id: str, answer: QuestionsUsersAnswer):
    query = f"""
        UPDATE {TABLE_NAME} 
        SET question_id = :question_id,
        user_id = :user_id,
        answer = :answer
        WHERE id = : answer_id
    """
    values = {
        "answer_id": answer_id,
        "question_id": answer.question_id,
        "user_id": answer.user_id,
        "answer": answer.answer
    }

    await database.execute(query, values)


async def delete_answer_by_id(answer_id: int):
    query = f"DELETE FROM {TABLE_NAME} WHERE id=:answer_id"
    return await database.execute(query, values={"question_id": answer_id})


# async def get_nuber_users_answered_each_option_in_question(question_id: int) -> Optional[int]:
#
#
# async def get_users_answered_question(question_id: int) -> Optional[int]:
#
#
#
# async def user_answer_to_each_question(user_id: int) -> Optional[UserResponse]:

#
#
# async def questions_user_answered(user_id: int):
