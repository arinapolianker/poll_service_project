from typing import Optional, List

from model.question import Question
from repository import question_repository, questions_users_answer_repository


async def get_question_by_id(question_id: int) -> Optional[Question]:
    return await question_repository.get_question_by_id(question_id)


async def get_all_questions() -> Optional[List[Question]]:
    return await question_repository.get_all_questions()


async def create_question(question: Question) -> int:
    return await question_repository.create_question(question)


async def update_question_by_id(question_id: int, question: Question):
    await question_repository.update_question_by_id(question_id, question)


async def delete_question_by_id(question_id: int):
    await questions_users_answer_repository.delete_answers_by_question_id(question_id)
    await question_repository.delete_question_by_id(question_id)

