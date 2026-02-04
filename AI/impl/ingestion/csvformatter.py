import pandas as pd
from dotenv import load_dotenv

from AI.impl.modules.gitcrawler import GitCrawler

load_dotenv()
def format_csv(name):
    all_code = []
    crawler = GitCrawler()
    df = pd.read_csv(
        '../../../dataset/raw/'+name,
        usecols=["URL","Identifier","FileInfo",
                "n_microservices",
                "Developed by"])
    df = df[df['Developed by'].str.contains("Industry", na=False)]

    for _, row in df.iterrows():
        crawler.repo_url = row["URL"]
        repo_df = reconstruct_df(crawler, row)
        if not repo_df.empty:
            all_code.append(repo_df)
    final_df = pd.concat(all_code, ignore_index=True)
    final_df.to_csv('../../../dataset/formatted/'+name)



def reconstruct_df(crawler:GitCrawler, meta_row):
    repo_files = crawler.crawl_repo_code()
    rows = []
    for p in repo_files:
        try:
            content = p.read_text(errors="ignore")
        except RuntimeError:
            continue
        rows.append({
            "URL": meta_row["URL"],
            "Identifier": meta_row["Identifier"],
            "FileInfo": meta_row["FileInfo"],
            "n_microservices": meta_row["n_microservices"],
            "path": str(p),
            "code": content
        })
    print(pd.DataFrame(rows))
    return pd.DataFrame(rows)
format_csv("MicroservicesDataset.csv")
