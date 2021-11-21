from github import Github
from joblib import Parallel, delayed


def read_repos(txt):
    with open(txt, 'r') as f:
        repos = f.readlines()
        for i in range(len(repos)):
            repos[i] = repos[i].rstrip()
    return repos


def get_t(token):
    client = Github(token)
    return client.get_rate_limit().core.remaining


tokens = read_repos('tokens.txt')

res = Parallel(n_jobs=len(tokens))(delayed(get_t)(i) for i in tokens)
print(res)
