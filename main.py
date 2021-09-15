import os
from shutil import move as move_file
from git.repo.base import Repo


def read_repos(txt):
    with open(txt, 'r') as f:
        repos = f.readlines()
        for i in range(len(repos)):
            repos[i] = repos[i].rstrip()
    return repos


def create_folder(repo):
    if not os.path.exists("repos"):
        os.mkdir("repos")
    if not os.path.exists(f"repos/{repo}"):
        os.mkdir(f"repos/{repo}")
    if not os.path.exists(f"repos/{repo}/src"):
        os.mkdir(f"repos/{repo}/src")
    if not os.path.exists(f"repos/{repo}/data"):
        os.mkdir(f"repos/{repo}/data")


def clone_repos(repos, not_clone=False):
    length = len(repos)
    for i, repo in enumerate(repos):
        spl = repo.split("/")
        name_repo = spl[len(spl) - 1]
        create_folder(name_repo)
        if not not_clone:
            try:
                Repo.clone_from(repo + ".git", f"repos/{name_repo}/src")
            except Exception as e:
                print(e)
            print(f"{(i + 1) / length * 100}%")


def generate_data(repos):
    length = len(repos)
    files = ["class.csv", "field.csv", "method.csv", "variable.csv"]
    for i, repo in enumerate(repos):
        spl = repo.split("/")
        name_repo = spl[len(spl) - 1]
        os.system(f"java -jar ck-0.6.5-SNAPSHOT-jar-with-dependencies.jar repos/{name_repo}/src true 0 True repos/{name_repo}/data")
        for file in files:
            print("Moving files")
            move_file(file, f"repos/{name_repo}/data/{file}")
        print(f"{(i + 1) / length * 100}%")


if __name__ == "__main__":
    repos = read_repos("repos.txt")
    clone_repos(repos, not_clone=True)
    generate_data(repos)
