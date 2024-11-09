import requests
import random
import pyperclip
import time
from colorama import Style, Fore

charset = 'ABCDEFGHIJKLMNOPabcdefghijklmnop1234567!@#*'


def authenticate_user(project_id: int) -> bool | tuple:
    author = requests.get(f"https://api.scratch.mit.edu/projects/{project_id}").json()["author"]["username"]
    code = ""
    for _ in range(15):
        code += str(charset[random.randint(0, len(charset) - 1)])
    print(
        f"Here is your auth code: {Style.BRIGHT + Fore.BLUE}{code}{Style.RESET_ALL} it has been automatically copied to your clipboard\nGo to https://scratch.mit.edu/projects/{project_id} and paste your code in the comments")
    pyperclip.copy(code)
    start = time.time()
    while True:
        comments = requests.get(f"https://api.scratch.mit.edu/users/{author}/projects/{project_id}/comments/").json()
        for number in range(len(comments)):
            if comments[number]['content'] == code:
                print(f"User {comments[number]['author']['username']} has authenticated")
                return True, comments[number]['author']['username']
        time.sleep(0.5)

        if time.time() - start > 120:
            print("Authentication timed out, please try again")
            return False
