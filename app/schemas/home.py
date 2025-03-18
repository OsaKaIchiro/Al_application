from pydantic import BaseModel
from typing import Union, Optional, Any

class GetMoney(BaseModel):
    username: str
    credits: Optional[int] = 0