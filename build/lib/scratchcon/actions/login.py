import scratchattach as sa
from .common import public
from scratchcon import exceptions


def login(username: str, password: str):
    try:
        public.login = sa.login(username, password)
    except exceptions.FailedToLogin as e:
        print(e)
