from fastapi import APIRouter, HTTPException

from model.question import Question
from service import question_service

router = APIRouter(
    prefix="/question",
    tags=["question"]
)


@router.get("/{question_id}", response_model=Question)
async def get_question_by_id(question_id: int):
    question = await question_service.get_question_by_id(question_id)
    if not question:
        raise HTTPException(status_code=404, detail=f"User with id:{question_id} not found...")
    else:
        return question


@router.post("/", response_model=Question)
async def create_question(question: Question):
    question_id = await question_service.create_question(question)
    return await question_service.get_question_by_id(question_id)


@router.put("/{question_id}", response_model=Question)
async def update_question_by_id(question_id: int, question: Question):
    question_exists = await question_service.get_question_by_id(question_id)
    if not question_exists:
        raise HTTPException(status_code=404, detail=f"Can't update question with id:{question_id}, question not found...")
    await question_service.update_question_by_id(question_id, question)
    return await question_service.get_question_by_id(question_id)


@router.delete("/{question_id}")
async def delete_question_by_id(question_id: int):
    question_exists = await question_service.get_question_by_id(question_id)
    if not question_exists:
        raise HTTPException(status_code=404, detail=f"Can't delete question with id:{question_id}, question not found...")
    await question_service.delete_question_by_id(question_id)

