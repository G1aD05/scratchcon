import requests
from .exceptions import *
from .common import public
from urllib.request import urlretrieve


class Project:
    @staticmethod
    def get_title():
        response = requests.get(public.project_link)
        if response.ok:
            return response.json()["title"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve project title: {response.status_code}")

    @staticmethod
    def get_description():
        response = requests.get(public.project_link)
        if response.ok:
            return response.json()["description"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve project description: {response.status_code}")

    @staticmethod
    def get_instructions():
        response = requests.get(public.project_link)
        if response.ok:
            return response.json()["instructions"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve project instructions: {response.status_code}")

    @staticmethod
    def get_author():
        response = requests.get(public.project_link)
        if response.ok:
            return response.json()["author"]["username"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve project author: {response.status_code}")

    @staticmethod
    def get_author_id():
        response = requests.get(public.project_link)
        if response.ok:
            return response.json()["author"]["id"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve project author ID: {response.status_code}")

    @staticmethod
    def get_creation_date():
        response = requests.get(public.project_link)
        if response.ok:
            return response.json()["history"]["created"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve project creation date: {response.status_code}")

    @staticmethod
    def get_share_date():
        response = requests.get(public.project_link)
        if response.ok:
            return response.json()["history"]["shared"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve project share date: {response.status_code}")

    @staticmethod
    def get_love_count():
        response = requests.get(public.project_link)
        if response.ok:
            return response.json()["stats"]["loves"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve project heart count: {response.status_code}")

    @staticmethod
    def get_view_count():
        response = requests.get(public.project_link)
        if response.ok:
            return response.json()["stats"]["views"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve project view count: {response.status_code}")

    @staticmethod
    def get_favorite_count():
        response = requests.get(public.project_link)
        if response.ok:
            return response.json()["stats"]["favorites"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve project favorite count: {response.status_code}")

    @staticmethod
    def get_remix_count():
        response = requests.get(public.project_link)
        if response.ok:
            return response.json()["stats"]["remixes"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve project remix count: {response.status_code}")

    @staticmethod
    def get_remixes():
        response = requests.get(f"{public.project_link}/remixes")
        if response.ok:
            return response.json()
        else:
            raise FailedToRetrieve(f"Failed to retrieve project remixes: {response.status_code}")

    @staticmethod
    def get_comments():
        response = requests.get(f"https://api.scratch.mit.edu/users/{requests.get(public.project_link).json()["author"]["username"]}/projects/{public.project_id}/comments")
        if response.ok:
            return response.json()
        else:
            raise FailedToRetrieve(f"Failed to retrieve project comments: {response.status_code}")

    @staticmethod
    def download_thumbnail(filename: str, size: str = "282x218"):
        urlretrieve(requests.get(f"{public.project_link}").json()["images"][size], filename)
