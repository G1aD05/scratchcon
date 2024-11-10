from scratchcon.actions.common import public
import requests


class Filter:
    def __init__(self, target_project: int, keywords: list[str] = None, preset: str = None):
        self.project = public.login.connect_project(str(target_project))
        self.project_comments = requests.get(
            f'https://api.scratch.mit.edu/users/{requests.get(f"https://api.scratch.mit.edu/projects/{target_project}").json()["author"]["username"]}/projects/{target_project}/comments').json()
        self.target_project = target_project
        self.keywords = None
        if preset is not None:
            if preset == "light":
                self.keywords = ['f4f', 'scratch.mit.edu/projects']
            elif preset == "medium":
                self.keywords = ['f4f', 'scratch.mit.edu/projects', 'trash', 'sucks']
            elif preset == "hard":
                self.keywords = ['f4f', 'scratch.mit.edu/projects', 'trash', 'sucks', 'terrible', 'i hate this']
            else:
                print("Preset not found")
        else:
            self.keywords = keywords

    def start_filter(self):
        while True:
            self.project_comments = requests.get(
                f'https://api.scratch.mit.edu/users/{requests.get(f"https://api.scratch.mit.edu/projects/{self.target_project}").json()["author"]["username"]}/projects/{self.target_project}/comments').json()
            for comment in self.project_comments:
                for key in self.keywords:
                    if str(key).lower() in comment['content'].lower():
                        print(f"Found \"{comment['content']}\"")
                        self.project.delete_comment(comment_id=str(comment['id']))
                    else:
                        pass
