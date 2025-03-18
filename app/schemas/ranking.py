from pydantic import BaseModel

class MoneyRanking(BaseModel):
    rank: int
    username: str
    credits: int