from google.genai import types
from google import genai
from typing import Any, List, Optional

from google.genai.types import ThinkingLevel
from pydantic import BaseModel

class Agent(BaseModel):
    name : str
    context : str
    microservices : Optional[List[str]] = ""
    userPreferences : Optional[str] = ""
    client : Any

    def response(self, message: str)-> str:
        prompt = ("This is the bussiness context the person whos is asking you is insered"
                + self.context
                + " this are their preferences in response "
                + self.userPreferences
                + "on base in this context and preferences, respond the user message,"
                + " focus on solving what he asked or helping"
                + " him understand what he wants to understand"
                + " be objective"
                + " message:"
                + message)
        response = self.client.models.generate_content(
            model="gemini-3-flash-preview",
            contents = prompt,
             config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_level=ThinkingLevel.MEDIUM)
            ),
        )
        return response.text
