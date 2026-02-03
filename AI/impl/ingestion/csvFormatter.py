import os

import pandas as pd
from github import Github, Auth
from dotenv import load_dotenv

load_dotenv()
def format_csv(name):
    connectGithub()
    df = pd.read_csv(
        '../../../dataset/raw/'+name,
        usecols=["URL","Identifier","FileInfo",
                "n_microservices","Application Type",
                "Application Purpose","Developed by"])
    df = df[df['Developed by'].str.contains("Industry", na=False)]
    repoLinksDf= df

    repo

    df.to_csv('../../../dataset/formatted/'+name)

def connectGithub():
    token = os.getenv("GITHUB_TOKEN")

    auth = Auth.Token(token)
    g = Github(auth=auth)
    g.get_user().login




format_csv("MicroservicesDataset.csv")
