from fastapi import APIRouter, HTTPException

from api.internalApi.user_service import user_service_api
from model.questions_users_answer import QuestionsUsersAnswer
from model.questions_users_answer_request import QuestionsUsersAnswerRequest
from model.questions_users_answer_response import QuestionsUsersAnswerResponse
from service import questions_users_answer_service, question_service

router = APIRouter(
    prefix="/answer",
    tags=["answer"]
)


@router.get("/{answer_id}", response_model=QuestionsUsersAnswerResponse)
async def get_answer_by_id(answer_id: int):
    answer = await questions_users_answer_service.get_answer_by_id(answer_id)
    if not answer:
        raise HTTPException(status_code=404, detail=f"Answer with id:{answer_id} not found...")
    else:
        return answer


@router.get("/", response_model=QuestionsUsersAnswerResponse)
async def get_answer_by_user_id_and_question_id(user_id: int, question_id: int):
    answer = await questions_users_answer_service.get_answer_by_question_id_and_user_id(user_id, question_id)
    if not answer:
        raise HTTPException(status_code=404, detail=f"Answer with user_id:{user_id} and question_id:{question_id} not found, user didn't answered question.")
    else:
        return answer


@router.post("/", response_model=QuestionsUsersAnswer)
async def create_answer(answer: QuestionsUsersAnswerRequest):
    answer_exists = await questions_users_answer_service.get_answer_by_question_id_and_user_id(answer.user_id, answer.question_id)
    if answer_exists:
        raise HTTPException(status_code=404, detail="User has already answered this question.")

    answer_id = await questions_users_answer_service.create_answer(answer)
    return await questions_users_answer_service.get_answer_by_id(answer_id)


@router.put("/{answer_id}", response_model=QuestionsUsersAnswer)
async def update_answer_by_answer_id(answer_id: int, answer: QuestionsUsersAnswer):
    answer_exists = await questions_users_answer_service.get_answer_by_id(answer_id)
    if not answer_exists:
        raise HTTPException(status_code=404, detail=f"Can't update answer with id:{answer_id}, answer not found...")
    if answer_exists.answer == answer.answer:
        raise HTTPException(status_code=404, detail=f"Can't update the answer to '{answer.answer}', this answer already exists.")

    await questions_users_answer_service.update_answer_by_answer_id(answer_id, answer)
    return await questions_users_answer_service.get_answer_by_id(answer_id)


@router.put("/update_answer/", response_model=QuestionsUsersAnswer)
async def update_answer_by_question_and_user_id(user_id: int, question_id: int, answer: str):
    answer_exists = await questions_users_answer_service.get_answer_by_question_id_and_user_id(user_id, question_id)
    if not answer_exists:
        raise HTTPException(status_code=404, detail=f"Can't update the answer for question id:{question_id}, answer not found...")
    if answer_exists.answer == answer:
        raise HTTPException(status_code=404, detail=f"Can't update the answer to '{answer}', it's the answer that exists.")

    await questions_users_answer_service.update_answer_by_question_and_user_id(user_id, question_id, answer)
    return await questions_users_answer_service.get_answer_by_question_id_and_user_id(user_id, question_id)


@router.delete("/{answer_id}")
async def delete_answer_by_answer_id(answer_id: int):
    answer_exists = await questions_users_answer_service.get_answer_by_id(answer_id)
    if not answer_exists:
        raise HTTPException(status_code=404, detail=f"Can't delete answer with id:{answer_id}, answer not found...")
    await questions_users_answer_service.delete_answer_by_id(answer_id)


@router.delete("/cleanup/")
async def delete_answers_for_none_existent_users_and_questions():
    existing_users = await user_service_api.get_all_users_id()
    existing_questions = [question.id for question in await question_service.get_all_questions()]
    if not existing_users or not existing_questions:
        raise HTTPException(status_code=404, detail=f"Can't delete answers, there is a user that still exists.")
    await questions_users_answer_service.delete_answers_for_none_existent_users_and_questions(existing_users, existing_questions)


@router.get("/count_answers_per_question/{question_id}")
async def get_answers_counts_by_question_id(question_id: int):
    answer_counts = await questions_users_answer_service.get_answers_counts_by_question_id(question_id)
    if answer_counts is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return answer_counts


@router.get("/total_answers_for_question/{question_id}")
async def get_total_users_answers_by_question_id(question_id: int):
    question_exists = await question_service.get_question_by_id(question_id)
    if not question_exists:
        raise HTTPException(status_code=404, detail="Question not found")
    return await questions_users_answer_service.get_total_users_answers_by_question_id(question_id)


@router.get("/user_answer_for_question/{user_id}")
async def get_user_answer_to_each_question(user_id: int):
    user_answers = await questions_users_answer_service.get_user_answer_to_each_question(user_id)
    if not user_answers:
        raise HTTPException(status_code=404, detail="No answers found, user not exists.")
    return user_answers


@router.get("/total_questions_user_answered/{user_id}")
async def get_total_questions_user_answered(user_id: int):
    total_answered_questions = await questions_users_answer_service.get_total_questions_user_answered(user_id)
    if not total_answered_questions:
        raise HTTPException(status_code=404, detail="User not found.")
    return total_answered_questions


@router.get("/all_questions_with_answers_count/")
async def get_all_questions_with_answers_count():
    return await questions_users_answer_service.get_all_questions_with_answers_count()

