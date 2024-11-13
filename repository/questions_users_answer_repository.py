from typing import Optional, List

from model.questions_users_answer import QuestionsUsersAnswer
from repository.database import database

TABLE_NAME = "questions_users_answer"


async def get_answer_by_id(answer_id: int) -> Optional[QuestionsUsersAnswer]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id=:answer_id"
    result = await database.fetch_one(query, values={"answer_id": answer_id})
    if result:
        return QuestionsUsersAnswer(**result)
    else:
        return None


async def get_answer_by_question_id_and_user_id(question_id: int, user_id: int) -> Optional[QuestionsUsersAnswer]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE question_id=:question_id AND user_id=:user_id LIMIT 1"
    result = await database.fetch_one(query, values={"question_id": question_id, "user_id": user_id})
    if result:
        return QuestionsUsersAnswer(**result)
    else:
        return None


async def create_answer(answer: QuestionsUsersAnswer) -> Optional[int]:
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


async def update_answer_by_answer_id(answer_id: int, answer: QuestionsUsersAnswer):
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


async def update_answer_by_question_and_user_id(question_id: int, user_id: id, answer: str):
    query = f"""
        UPDATE {TABLE_NAME}
        SET answer = :answer
        WHERE question_id = :question_id
        AND user_id = :user_id
    """
    values = {
        "question_id": question_id,
        "user_id": user_id,
        "new_answer": answer,
    }
    await database.execute(query, values)


async def delete_answer_by_id(answer_id: int):
    query = f"DELETE FROM {TABLE_NAME} WHERE id=:answer_id"
    await database.execute(query, values={"answer_id": answer_id})


async def delete_answers_for_none_existent_users_and_questions(existing_users):
    if not existing_users:
        return None

    query = f"""
    DELETE FROM {TABLE_NAME}
    WHERE question_id NOT IN (SELECT id FROM question)
    OR user_id NOT IN :existing_users
    """
    await database.execute(query, values={"existing_users": tuple(existing_users)})


async def get_answers_counts_by_question_id(question_id: int):
    query = f"""
        SELECT answer, COUNT(*) as count
        FROM {TABLE_NAME} 
        WHERE question_id = :question_id
        GROUP BY answer
    """
    return await database.fetch_all(query, values={"question_id": question_id})


async def get_total_users_answers_by_question_id(question_id: int) -> Optional[int]:
    query = f"""
        SELECT COUNT(*) as total
        FROM {TABLE_NAME} 
        WHERE question_id = :question_id
    """
    result = await database.fetch_one(query, values={"question_id": question_id})
    return result if result else None


async def get_user_answer_to_each_question(user_id: int) -> Optional[List]:
    query = f"""
        SELECT question_id, answer
        FROM {TABLE_NAME}
        WHERE user_id = :user_id
    """

    results = await database.fetch_all(query, values={"user_id": user_id})
    answer_chosen = []
    for row in results:
        question_query = "SELECT title, a, b, c, d FROM question WHERE id = :question_id"
        question_result = await database.fetch_one(question_query, values={"question_id": row["question_id"]})

        if question_result:
            answer_key = row["answer"]
            answer_text = question_result[answer_key]
            answer_chosen.append({question_result["title"]: {"answer": answer_text}})

    return answer_chosen


async def get_total_questions_user_answered(user_id: int) -> Optional[int]:
    query = f"""
        SELECT COUNT(*) as total
        FROM {TABLE_NAME} 
        WHERE user_id = :user_id
    """
    result = await database.fetch_one(query, values={"user_id": user_id})
    if result is None or result["total"] == 0:
        return None
    return result


async def get_all_questions_with_answers_count():
    query = f"""
        SELECT question_id, answer, COUNT(*) as count
        FROM {TABLE_NAME} 
        GROUP BY question_id, answer
    """
    return await database.fetch_all(query)
