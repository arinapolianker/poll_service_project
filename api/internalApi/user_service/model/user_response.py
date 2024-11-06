from datetime import date
from typing import Optional

from pydantic import BaseModel


class UserResponse(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    age: int
    address: str
    joining_date: date
    registered: bool
