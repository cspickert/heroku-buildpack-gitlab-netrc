import json
import subprocess
from functools import lru_cache


def valid_login(token):
    return login(token) != "error"


@lru_cache
def login(token):
    return gitlab_user_login(token)


def gitlab_user_login(token):
    try:
        resp = subprocess.check_output(
            [
                "curl",
                "-H",
                f"Private-Token: {token}",
                "-s",
                "https://gitlab.com/api/v4/user",
            ]
        )
        user = json.loads(resp)
        return user["username"]
    except Exception as exc:
        print(exc)
        return "error"


def user_block(token):
    return f"       Gitlab User:   {login(token)}"
