from langchain_community.document_loaders.csv_loader import CSVLoader


def main():
    loader = CSVLoader(
        file_path="../../dataset/formatted/MicroservicesDataset.csv",
    )
    for document in loader.lazy_load():
        print(document)
main()