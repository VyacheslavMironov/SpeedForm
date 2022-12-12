from typing import Protocol
from profiles.application.domain.model.user import UserRequest


class NotInUserPort(Protocol):
    def not_in_user(self) -> UserRequest:
        raise Exception('Нет такого пользователя!')
https://github.com/BasicWolf/hexagonal-architecture-django/blob/main/src/myapp/application/adapter/api/http/serializer/successfully_voted_result_serializer.py