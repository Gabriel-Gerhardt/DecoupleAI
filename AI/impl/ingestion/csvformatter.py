import pandas as pd
from dotenv import load_dotenv
from anthropic import Anthropic
from AI.impl.modules.clauderesumegenerator import ClaudeResumeGenerator
from AI.impl.modules.gitcrawler import GitCrawler

load_dotenv()
def format_csv(name):
    crawler = GitCrawler()
    client = Anthropic()
    resume_generator = ClaudeResumeGenerator(client=client)
    df = pd.read_csv(
        '../../../dataset/raw/'+name,
        usecols=["URL","Identifier","FileInfo",
                "n_microservices",
                "Developed by"])
    df = df[df['Developed by'].str.contains("Industry", na=False)]
    resumes = []
    row = df.iloc[0]

    crawler.repo_url = row["URL"]
    crawler.path = "../../../repos"

    repo_df = reconstruct_df(crawler, row)

    if repo_df.empty:
        return

    resume = generate_df_resume(repo_df, resume_generator)

    final_resume_df = pd.DataFrame([{
        "URL": row["URL"],
        "Identifier": row["Identifier"],
        "FileInfo": row["FileInfo"],
        "n_microservices": row["n_microservices"],
        "resume": resume,
    }])

    final_resume_df.to_csv(
        "../../../dataset/formatted/repo_resumes.csv",
        index=False,
    )


def reconstruct_df(crawler: GitCrawler, meta_row):
    repo_files = crawler.crawl_repo_code()
    rows = []

    for p in repo_files:
        try:
            content = p.read_text(errors="ignore")
        except RuntimeError:
            continue

        rows.append(
            {
                "URL": meta_row["URL"],
                "Identifier": meta_row["Identifier"],
                "FileInfo": meta_row["FileInfo"],
                "n_microservices": meta_row["n_microservices"],
                "path": str(p),
                "code": content,
            }
        )

    return pd.DataFrame(rows)


def generate_df_resume(df: pd.DataFrame, generator: ClaudeResumeGenerator):
    meta = df.iloc[0]

    chunks = [
        f"REPO: {meta['URL']}\n"
        f"IDENTIFIER: {meta['Identifier']}\n"
        f"FILEINFO: {meta['FileInfo']}\n"
        f"MICROSERVICES: {meta['n_microservices']}\n"
    ]

    for _, row in df.iterrows():
        chunks.append(
            f"\nFILE: {row['path']}\n"
            f"{row['code']}\n"
        )

    prompt = "".join(chunks)
    return generator.generateresume(prompt)


format_csv("MicroservicesDataset.csv")
