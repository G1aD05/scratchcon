from .exceptions import *
import requests
from .common import public


class User:
    @staticmethod
    def get_status():
        response = requests.get(public.user_link)
        if response.ok:
            return response.json()["profile"]["status"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve user status: {response.status_code}")

    @staticmethod
    def get_message_count():
        response = requests.get(f"{public.user_link}/messages/count")
        if response.ok:
            return response.json()["count"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve user message count: {response.status_code}")

    @staticmethod
    def get_id():
        response = requests.get(public.user_link)
        if response.ok:
            return response.json()["id"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve user ID: {response.status_code}")

    @staticmethod
    def get_bio():
        response = requests.get(public.user_link)
        if response.ok:
            return response.json()["profile"]["bio"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve user bio: {response.status_code}")

    @staticmethod
    def get_country():
        response = requests.get(public.user_link)
        if response.ok:
            return response.json()["profile"]["country"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve user country: {response.status_code}")

    @staticmethod
    def get_username():
        response = requests.get(public.user_link)
        if response.ok:
            return response.json()["username"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve user username: {response.status_code}")

    @staticmethod
    def get_join_date():
        response = requests.get(public.user_link)
        if response.ok:
            return response.json()["history"]["joined"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve user join date: {response.status_code}")

    @staticmethod
    def is_st():
        response = requests.get(public.user_link)
        if response.ok:
            return response.json()["scratchteam"]
        else:
            raise FailedToRetrieve(f"Failed to retrieve user Scratch Team status: {response.status_code}")
