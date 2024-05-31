from pydantic import BaseModel

class President(BaseModel):
    id: int
    image: str
    name: str
    lastName: str
    startPeriodDate: str
    endPeriodDate: str
    politicalParty: str
    description: str
