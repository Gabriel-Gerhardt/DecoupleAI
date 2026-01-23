import os

from dotenv import load_dotenv
from google import genai

from AI.impl.agents.agent import Agent


def main():
    load_dotenv()
    key = os.getenv("API_KEY")
    client = genai.Client(api_key=key)
    agent = Agent(name="daboss",
                  context="Pfizer Inc. is an American multinational pharmaceutical and biotechnology company headquartered in New York City. It is one of the world’s largest research-based pharmaceutical firms and has existed since 1849, focusing on the discovery, development, manufacturing, and marketing of medicines and vaccines for humans and animals. Pfizer develops treatments across many therapeutic areas including immunology, oncology (cancer), cardiology (heart health), endocrinology (hormones), and neurology (brain and nervous system). Its product portfolio includes widely used medications such as antidepressants, cardiovascular drugs, vaccines like the Comirnaty COVID‑19 vaccine, and many over‑the‑counter products. The company operates globally, selling its products in nearly 200 countries with tens of thousands of employees and a large research‑and‑development pipeline.",
                  client=client)
    response = agent.response("can you explain a little bit my corporation and what i can expect to find in their microservices?")
    print(response)

main()