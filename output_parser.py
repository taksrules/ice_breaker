from pydantic import BaseModel,Field
from  typing import List

class PersonIntel(BaseModel):
    summary:str= Field(description="Summary of Person")
    facts:List[str]= Field(description="")