import os
from shutil import move as move_file
from shutil import copytree as copy_folder
from git.repo.base import Repo


def read_repos(txt):
    with open(txt, 'r') as f:
        repos = f.readlines()
        for i in range(len(repos)):
            repos[i] = repos[i].rstrip()
    return repos


def create_folder(repo, root_folder="repos", src=True, data=True):
    if not os.path.exists(root_folder):
        os.mkdir(root_folder)
    if not os.path.exists(f"{root_folder}/{repo}"):
        os.mkdir(f"{root_folder}/{repo}")
    if src:
        if not os.path.exists(f"{root_folder}/{repo}/src"):
            os.mkdir(f"{root_folder}/{repo}/src")
    if data:
        if not os.path.exists(f"{root_folder}/{repo}/data"):
            os.mkdir(f"{root_folder}/{repo}/data")


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
        os.system(
            f"java -jar ck-0.6.5-SNAPSHOT-jar-with-dependencies.jar repos/{name_repo}/src true 0 True repos/{name_repo}/data")
        for file in files:
            print("Moving files")
            move_file(file, f"repos/{name_repo}/data/{file}")
        print(f"{(i + 1) / length * 100}%")


def grab_csv(repos):
    for repo in repos:
        spl = repo.split("/")
        name_repo = spl[len(spl) - 1]
        copy_folder(f"repos/{name_repo}/data", f"csv/{name_repo}/data")


if __name__ == "__main__":
    repos = read_repos("repos.txt")
    clone_repos(repos, not_clone=False)
    generate_data(repos)
    grab_csv(repos)
