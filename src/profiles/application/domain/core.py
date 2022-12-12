from typing import NewType


UserCreate = NewType('UserCreate', dict)
UserShow = NewType('UserShow', dict)
BearerToken = NewType('BearerToken', str)
