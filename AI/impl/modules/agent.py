from typing import Any, List, Optional

from pydantic import BaseModel

class Agent(BaseModel):
    name : str
    context : str
    userPreferences : Optional[str] = ""
    client : Any
