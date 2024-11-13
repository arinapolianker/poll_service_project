from fastapi import FastAPI

from repository.database import database
from controller.question_controller import router as question_router
from controller.questions_users_answer_controller import router as answer_router

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(question_router)
app.include_router(answer_router)
