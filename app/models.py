from pydantic import BaseModel
from typing import Optional, Dict

class ResumeFetchRequest(BaseModel):
    github: Optional[str]
    linkedin: Optional[str]
    scholar: Optional[str]

class ResumeData(BaseModel):
    linkedin: Optional[Dict] = None
    github: Optional[Dict] = None
    scholar: Optional[Dict] = None
