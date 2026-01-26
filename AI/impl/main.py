import os

from dotenv import load_dotenv
from langchain_community.document_loaders.csv_loader import CSVLoader


#from AI.impl.agents.agent import Agent


def main():
    loader = CSVLoader(
        file_path="../../dataset/formatted/MicroservicesDataset.csv",
    )
    load_dotenv()
    key = os.getenv("API_KEY")
    for document in loader.lazy_load():
        print(document)
    print(key)
main()