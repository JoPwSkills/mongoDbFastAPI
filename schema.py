# data validation

from pydantic import BaseModel, Field
from typing import List, Dict, Annotated

class MongoDBSchema(BaseModel):
    user_id: int
    bio : Annotated[str, Field(example = 'AI engineer')]
    interests: Annotated[List[str], Field(example = ['LLM'])]
    social_link: Annotated[Dict[str, str], Field(example = {'github' : "https://github.com/username"})]
