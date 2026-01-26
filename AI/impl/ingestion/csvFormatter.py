import pandas as pd


def format_csv(name):
    df = pd.read_csv(
        '../../../dataset/raw/'+name,
        usecols=["URL","Identifier","FileInfo",
                "n_microservices","Application Type",
                "Application Purpose","Developed by"])

    df.to_csv('../../../dataset/formatted/'+name)

format_csv("MicroservicesDataset.csv")