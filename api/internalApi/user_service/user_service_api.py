from typing import Optional, List

import httpx

from api.internalApi.user_service.model.user_response import UserResponse
from config.config import Config

config = Config()


async def get_user_by_user_id(user_id) -> Optional[UserResponse]:
    url = f"{config.USER_SERVICE_BASE_URL}/user/{user_id}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            user_response = UserResponse(
                id=data.get("id"),
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                email=data.get("email"),
                age=data.get("age"),
                address=data.get("address"),
                joining_date=data.get("joining_date"),
                registered=data.get("registered"),
            )
            return user_response

        except httpx.HTTPStatusError as exception:
            print(f"Error in getting user '{user_id}'. error: {exception.response}")
            return None


async def get_all_users_id() -> Optional[List[int]]:
    url = f"{config.USER_SERVICE_BASE_URL}/user"
    async with httpx.AsyncClient(follow_redirects=True) as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            all_users_response = [user['id'] for user in data]
            return all_users_response

        except httpx.HTTPStatusError as exception:
            print(f"Error in getting all users. error: {exception.response}")
            return None
