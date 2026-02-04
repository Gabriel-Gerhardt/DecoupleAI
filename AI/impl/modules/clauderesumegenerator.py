import os

import dotenv
from anthropic import Anthropic
from anthropic.types import MessageParam
from pydantic import BaseModel


dotenv.load_dotenv()
class ClaudeResumeGenerator(BaseModel):
    client : Anthropic

    def generateresume(self, data : str):

        prompt_base = os.getenv("AI_PROMPT", "")
        messages = [
            MessageParam(role="user",content=prompt_base + data),
        ]
        message = self.client.messages.create(
            model="claude-4-5",
            max_tokens=8000,
            messages=messages
        )
        return message["completion"]