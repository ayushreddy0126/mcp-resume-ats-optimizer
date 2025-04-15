from pydantic import BaseModel
from typing import List, Optional, Dict

class ResumeFetchRequest(BaseModel):
    platforms: List[str]
    username: str

class ResumeData(BaseModel):
    linkedin: Optional[Dict] = None
    github: Optional[Dict] = None
    scholar: Optional[Dict] = None