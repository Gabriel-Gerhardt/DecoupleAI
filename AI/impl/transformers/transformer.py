from typing import Any

from langchain_text_splitters import RecursiveCharacterTextSplitter
from pydantic import BaseModel


class DecoupleTransformer(BaseModel):
    splitter : Any

    def create_splitter(self):
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    def split(self, docs):
        final_docs = self.splitter.split_documents(docs)
        return final_docs

