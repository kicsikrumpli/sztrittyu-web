from typing import List

from pydantic import BaseModel


class Req(BaseModel):
    name: str
    url: str


class Reqs(BaseModel):
    items: List[Req]