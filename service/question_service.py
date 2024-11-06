from typing import Optional

from model.question import Question
from repository import question_repository


async def get_question_by_id(question_id: int) -> Optional[Question]:
    return await question_repository.get_question_by_id(question_id)


async def create_question(question: Question) -> int:
    return await question_repository.create_question(question)


async def update_question_by_id(question_id: int, question: Question):
    await question_repository.update_question_by_id(question_id, question)


async def delete_question_by_id(question_id: int):
    await question_repository.delete_question_by_id(question_id)

