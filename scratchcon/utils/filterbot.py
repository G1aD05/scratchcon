from scratchcon.actions.common import public
import requests


class Filter:
    def __init__(self, target_project: int, keywords: list[str]):
        self.project = public.login.connect_project(str(target_project))
        self.project_comments = requests.get(
            f'https://api.scratch.mit.edu/users/{requests.get(f"https://api.scratch.mit.edu/projects/{target_project}").json()["author"]["username"]}/projects/{target_project}/comments').json()
        self.target_project = target_project
        self.keywords = keywords

    def start_filter(self):
        while True:
            self.project_comments = requests.get(
                f'https://api.scratch.mit.edu/users/{requests.get(f"https://api.scratch.mit.edu/projects/{self.target_project}").json()["author"]["username"]}/projects/{self.target_project}/comments').json()
            for comment in self.project_comments:
                for key in self.keywords:
                    if str(key) in comment['content']:
                        print(f"Found \"{comment['content']}\"")
                        self.project.delete_comment(comment_id=str(comment['id']))
                    else:
                        pass
