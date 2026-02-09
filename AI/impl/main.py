from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from AI.impl.transformers.transformer import DecoupleTransformer


def main():
    loader = CSVLoader(
        file_path="../../dataset/formatted/MicroservicesDataset.csv",
    )
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    split_docs =splitter.split_documents(docs)
    print(split_docs)


main()