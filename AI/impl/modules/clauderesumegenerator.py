import os
from typing import Any

from anthropic.types import MessageParam
from pydantic import BaseModel


class ClaudeResumeGenerator(BaseModel):
    client : Any

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