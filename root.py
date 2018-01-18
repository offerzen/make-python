import os
import requests

BASE_URL = "https://sandbox.root.co.za/v1/insurance"
ROOT_APP_ID = os.environ.get('ROOT_APP_ID')
ROOT_APP_SECRET = os.environ.get('ROOT_APP_SECRET')


class RootException(Exception):
    pass


def list_gadget_models():
    result = requests.get(f"{BASE_URL}/gadgets/models", auth=(ROOT_APP_ID, ROOT_APP_SECRET))
    if result.status_code == 200:
        return result.json()
    else:
        raise RootException()
