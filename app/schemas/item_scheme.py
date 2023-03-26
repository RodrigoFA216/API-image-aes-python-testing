from typing import Optional
from enum import Enum
from pydantic import BaseModel, Field


class ItemScheme(BaseModel):
    x1: list[int] = Field([-1, -1, 1, 1], title='Bit 1')
    x2: list[int] = Field([-1, 1, -1, 1], title='Bit 2')
    th: float = Field(None, title='Theta')
    w1: float = Field(None, title='Weight 1')
    w2: float = Field(None, title='Weight 2')
    gate: str = Field('And', title='Logic Gate')
