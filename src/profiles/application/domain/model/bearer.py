from __future__ import annotations
from dataclasses import dataclass

from rest_framework_simplejwt.tokens import RefreshToken


@dataclass
class SetBearerToken:
    bearerToken: RefreshToken

@dataclass
class GetBearerToken:
    bearerToken: RefreshToken

