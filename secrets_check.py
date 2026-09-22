import os

SECRET_NAMES = ["DOCKER_API_TOKEN", "MONITOR_ACCESS_KEY"]


def check_secrets():
    result = {}
    for name in SECRET_NAMES:
        value = os.getenv(name)
        result[name] = "задан" if value else "не задан"
    return result
