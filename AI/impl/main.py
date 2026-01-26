import os

from dotenv import load_dotenv

from AI.impl.agents.agent import Agent


def main():
    load_dotenv()
    key = os.getenv("API_KEY")
    print("hello")
    print(key)
main()