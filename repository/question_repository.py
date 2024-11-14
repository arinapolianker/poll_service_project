from typing import Optional, List

from model.question import Question
from repository.database import database

TABLE_NAME = "question"


async def get_question_by_id(question_id: int) -> Optional[Question]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id=:question_id"
    result = await database.fetch_one(query, values={"question_id": question_id})
    if result:
        return Question(**result)
    else:
        return None


async def get_all_questions() -> Optional[List[Question]]:
    query = f"SELECT * FROM {TABLE_NAME}"
    results = await database.fetch_all(query)
    return [Question(**result) for result in results]


async def create_question(question: Question) -> int:
    query = f"""
        INSERT INTO {TABLE_NAME} (title, a, b, c, d)
        VALUES (:title, :a, :b, :c, :d)
    """
    values = {
        "title": question.title,
        "a": question.a,
        "b": question.b,
        "c": question.c,
        "d": question.d
    }
    async with database.transaction():
        await database.execute(query, values)
        last_record_id = await database.fetch_one("SELECT LAST_INSERT_ID()")
    return last_record_id[0] if last_record_id else None


async def update_question_by_id(question_id: int, question: Question):
    query = f"""
        UPDATE {TABLE_NAME} 
        SET title = :title,
        a = :a,
        b = :b,
        c = :c,
        d = :d
        WHERE id = :question_id
    """
    values = {
        "question_id": question_id,
        "title": question.title,
        "a": question.a,
        "b": question.b,
        "c": question.c,
        "d": question.d
    }
    await database.execute(query, values=values)


async def delete_question_by_id(question_id: int):
    query = f"DELETE FROM {TABLE_NAME} WHERE id=:question_id"
    return await database.execute(query, values={"question_id": question_id})



