from pydantic import BaseModel
from typing import Union, Optional, Any

class ContextPut(BaseModel):
    number: int
    username: int
    context: str