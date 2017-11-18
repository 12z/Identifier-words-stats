import os

from git import Repo
from git.exc import GitError

from .exc import RepositoryCloningError


REPOS_FOLDER_MODE = 0o775
REPOS_FOLDER_FULL_NAME = '/tmp/repos'


def download_repo(repo_url: str) -> str:
    repo_folder = construct_repo_folder(REPOS_FOLDER_FULL_NAME, repo_url)

    if os.path.exists(repo_folder):
        # already exists, do not clone again
        return repo_folder

    os.makedirs(REPOS_FOLDER_FULL_NAME, REPOS_FOLDER_MODE, exist_ok=True)
    try:
        Repo.clone_from(repo_url, repo_folder)
    except GitError as e:
        raise RepositoryCloningError().with_traceback(e.__traceback__)

    return repo_folder


def construct_repo_folder(repos_base_dir, repo_url):
    repo_name = repo_url.split('/')[-1]
    return os.path.join(repos_base_dir, repo_name)


if __name__ == '__main__':
    test_repo_url = 'https://github.com/gitpython-developers/GitPython'

    download_repo(test_repo_url)
