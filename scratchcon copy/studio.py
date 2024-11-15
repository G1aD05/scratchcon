from .exceptions import *
from .common import public
import requests
from urllib.request import urlretrieve


class Studio:
    @staticmethod
    def get_description():
        response = requests.get(public.studio_link)
        if response.ok:
            return response.json()["description"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve studio description: {response.status_code}")

    @staticmethod
    def get_curators():
        response = requests.get(f"{public.studio_link}/curators")
        if response.ok:
            return response.json()
        else:
            raise FailedToRetrieve(f"Failed to retrieve studio curators: {response.status_code}")

    @staticmethod
    def get_title():
        response = requests.get(public.studio_link)
        if response.ok:
            return response.json()["title"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve studio title: {response.status_code}")

    @staticmethod
    def get_creation_date():
        response = requests.get(public.studio_link)
        if response.ok:
            return response.json()["history"]["created"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve studio creation date: {response.status_code}")

    @staticmethod
    def get_project_amount():
        response = requests.get(f"{public.studio_link}")
        if response.ok:
            return len(response.json()["status"]["projects"])
        else:
            raise FailedToRetrieve(f"Failed to retrieve studio project amount: {response.status_code}")

    @staticmethod
    def get_follower_amount():
        response = requests.get(f"{public.studio_link}")
        if response.ok:
            return len(response.json()["status"]["followers"])
        else:
            raise FailedToRetrieve(f"Failed to retrieve studio follower amount: {response.status_code}")

    @staticmethod
    def get_managers():
        response = requests.get(f"{public.studio_link}")
        if response.ok:
            return response.json()["status"]["managers"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve studio managers: {response.status_code}")

    @staticmethod
    def get_comment_amount():
        response = requests.get(f"{public.studio_link}")
        if response.ok:
            return response.json()["status"]["comments"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve studio comment amount: {response.status_code}")

    @staticmethod
    def get_comments():
        response = requests.get(f"{public.studio_link}/comments")
        if response.ok:
            return response.json()
        else:
            raise FailedToRetrieve(f"Failed to retrieve studio comments: {response.status_code}")

    @staticmethod
    def get_projects():
        response = requests.get(f"{public.studio_link}/projects")
        if response.ok:
            return response.json()
        else:
            raise FailedToRetrieve(f"Failed to retrieve studio projects: {response.status_code}")

    @staticmethod
    def get_activity():
        response = requests.get(f"{public.studio_link}/activity")
        if response.ok:
            return response.json()
        else:
            raise FailedToRetrieve(f"Failed to retrieve studio activity: {response.status_code}")

    @staticmethod
    def download_thumbnail(filename: str):
        urlretrieve(requests.get(f"{public.studio_link}").json()["image"], filename)
