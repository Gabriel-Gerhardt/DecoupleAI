import os

from dotenv import load_dotenv

from agents.agent import Agent


def main():
    load_dotenv()
    key = os.getenv("API_KEY")
    print("hello")
    print(key)
main()