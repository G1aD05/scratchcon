import scratchcon.utils.auth as auth

authenticated: bool = False
username = ""

while not authenticated:
    authenticated, username = auth.authenticate_user(1041557087)

if username ==
