import os
from git.repo.base import Repo


def read_repos(txt):
    with open(txt, 'r') as f:
        repos = f.readlines()
        for i in range(len(repos)):
            repos[i] = repos[i].rstrip()
    return repos


def clone_repos(repos):
    length = len(repos)
    for i, repo in enumerate(repos):
        spl = repo.split("/")
        name_repo = spl[len(spl) - 1]
        if not os.path.exists("repos"):
            os.mkdir("repos")
        if not os.path.exists(f"repos/{name_repo}"):
            os.mkdir(f"repos/{name_repo}")
        if not os.path.exists(f"repos/{name_repo}/src"):
            os.mkdir(f"repos/{name_repo}/src")
        if not os.path.exists(f"repos/{name_repo}/data"):
            os.mkdir(f"repos/{name_repo}/data")
        try:
            Repo.clone_from(repo + ".git", f"repos/{name_repo}/src")
        except Exception as e:
            print(e)
        print(f"{(i+1)/length}%")


if __name__ == "__main__":
    repos = read_repos("repos.txt")
    clone_repos(repos)
