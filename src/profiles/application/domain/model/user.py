from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime


class UserRequest:
    pass

@dataclass
class UserRequestCreate(UserRequest):
    first_name: str
    last_name: str
    email: str
    password: str
    created_at: datetime

@dataclass
class UserRequestShow(UserRequest):
    email: str
    password: str
