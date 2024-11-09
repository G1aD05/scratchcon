from .common import public


def connect_project(proj_id):
    public.project_id = proj_id


def connect_studio(studio_id):
    public.studio_id = studio_id


def connect_user(username):
    public.username = username
