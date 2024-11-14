from .common import public


class Connect:

    @staticmethod
    def connect_user(user: str):
        public.user_link = f"https://api.scratch.mit.edu/users/{user}"

    @staticmethod
    def connect_project(project: int):
        public.project_id = project
        public.project_link = f"https://api.scratch.mit.edu/projects/{project}"

    @staticmethod
    def connect_studio(studio: int):
        public.studio_link = f"https://api.scratch.mit.edu/studios/{studio}"
