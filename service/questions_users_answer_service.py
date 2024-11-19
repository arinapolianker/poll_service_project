from typing import Optional, Dict, List

from fastapi import HTTPException

from api.internalApi.user_service import user_service_api
from model.questions_users_answer import QuestionsUsersAnswer
from model.questions_users_answer_request import QuestionsUsersAnswerRequest
from model.questions_users_answer_response import QuestionsUsersAnswerResponse
from repository import questions_users_answer_repository, question_repository
from service import question_service


async def options_mapping(question_id):
    question = await question_repository.get_question_by_id(question_id)
    if not question:
        return None

    choices_mapping = {
        "a": question.a,
        "b": question.b,
        "c": question.c,
        "d": question.d
    }
    return choices_mapping


async def answer_validation(answer: str, question_id: int) -> str:
    options = await options_mapping(question_id)
    if answer not in options:
        raise HTTPException(status_code=400, detail=f"Invalid answer. Select 'a', 'b', 'c', or 'd'.")
    else:
        return answer


async def get_answer_by_id(answer_id: int) -> Optional[QuestionsUsersAnswerResponse]:
    question_user_answer = await questions_users_answer_repository.get_answer_by_id(answer_id)
    if question_user_answer is not None:
        question_details = await question_service.get_question_by_id(question_user_answer.question_id)
        return QuestionsUsersAnswerResponse(
            id=question_user_answer.id,
            user_id=question_user_answer.user_id,
            question_id=question_user_answer.question_id,
            question_title=question_details.title,
            answer=question_user_answer.answer
        )
    return None


async def get_answer_by_question_id_and_user_id(user_id: int, question_id: int) -> Optional[QuestionsUsersAnswerResponse]:
    question_user_answer = await questions_users_answer_repository.get_answer_by_question_id_and_user_id(user_id, question_id)
    if question_user_answer is not None:
        question_details = await question_service.get_question_by_id(question_user_answer.question_id)
        return QuestionsUsersAnswerResponse(
            id=question_user_answer.id,
            user_id=question_user_answer.user_id,
            question_id=question_user_answer.question_id,
            question_title=question_details.title,
            answer=question_user_answer.answer
        )
    return None


async def create_answer(answer: QuestionsUsersAnswerRequest) -> Optional[int]:
    question_id = answer.question_id
    user_id = answer.user_id
    option_answer = answer.answer
    valid_answer = await answer_validation(option_answer, question_id)

    answer_exists = await questions_users_answer_repository.get_answer_by_question_id_and_user_id(question_id, user_id)

    if answer_exists:
        raise HTTPException(status_code=409, detail="User has already answered this question.")

    user_details = await user_service_api.get_user_by_user_id(user_id)
    if not user_details:
        raise HTTPException(status_code=404, detail=f"Can't find user with id: {user_id}")

    if not user_details.registered:
        raise HTTPException(status_code=403, detail="User isn't registered.")
    question_user_answer = QuestionsUsersAnswer(question_id=question_id, user_id=user_id, answer=valid_answer)
    return await questions_users_answer_repository.create_answer(question_user_answer)


async def update_answer_by_answer_id(answer_id: int, answer: QuestionsUsersAnswer):
    question_id = answer.question_id
    user_id = answer.user_id
    option_answer = answer.answer
    valid_answer = await answer_validation(option_answer, question_id)
    updated_answer = QuestionsUsersAnswer(question_id=question_id, user_id=user_id, answer=valid_answer)
    await questions_users_answer_repository.update_answer_by_answer_id(answer_id, updated_answer)


async def update_answer_by_question_and_user_id(user_id: int, question_id: int, answer: str):
    valid_answer = await answer_validation(answer, question_id)
    await questions_users_answer_repository.update_answer_by_question_and_user_id(user_id, question_id, valid_answer)


async def delete_answer_by_id(answer_id: int):
    answer = get_answer_by_id(answer_id)
    if not answer:
        await questions_users_answer_repository.delete_answer_by_id(answer_id)
    await questions_users_answer_repository.delete_answer_by_id(answer_id)


async def delete_answers_by_user_id(user_id: int):
    await questions_users_answer_repository.delete_answers_by_user_id(user_id)


async def get_answers_counts_by_question_id(question_id: int) -> Optional[Dict]:
    question = await question_repository.get_question_by_id(question_id)
    options = await options_mapping(question_id)

    answers_count = {
        options["a"]: 0,
        options["b"]: 0,
        options["c"]: 0,
        options["d"]: 0
    }

    results = await questions_users_answer_repository.get_answers_counts_by_question_id(question_id)

    for row in results:
        option_key = row["answer"]
        if option_key in options:
            option_text = options[option_key]
            answers_count[option_text] = row["count"]
    final_result = {question.title: answers_count}
    return final_result if final_result else None


async def get_total_users_answers_by_question_id(question_id: int) -> Optional[int]:
    return await questions_users_answer_repository.get_total_users_answers_by_question_id(question_id)


async def get_user_answer_to_each_question(user_id: int) -> Optional[List]:
    return await questions_users_answer_repository.get_user_answer_to_each_question(user_id)


async def get_total_questions_user_answered(user_id: int) -> Optional[int]:
    return await questions_users_answer_repository.get_total_questions_user_answered(user_id)


async def get_all_questions_with_answers_count() -> Optional[List]:
    results = await questions_users_answer_repository.get_all_questions_with_answers_count()

    all_questions_details = {}
    for row in results:
        question_id = row["question_id"]
        option_key = row["answer"]
        count = row["count"]
        question_details = await question_repository.get_question_by_id(question_id)

        if question_id not in all_questions_details:
            if question_details:
                all_questions_details[question_id] = {
                    "title": question_details.title,
                    "options": {
                        question_details.a: 0,
                        question_details.b: 0,
                        question_details.c: 0,
                        question_details.d: 0
                    }
                }

        if question_id in all_questions_details:
            options_map = {
                "a": question_details.a,
                "b": question_details.b,
                "c": question_details.c,
                "d": question_details.d,
            }

            option_text = options_map.get(option_key)
            if option_text:
                all_questions_details[question_id]["options"][option_text] = count

    result = []
    for details in all_questions_details.values():
        all_questions = {
            details["title"]: details["options"]
        }
        result.append(all_questions)

    return result
