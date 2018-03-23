import os
import requests
from settings import settings
from requests.auth import HTTPBasicAuth

BASE_URL = settings.BASE_URL
ROOT_APP_ID = settings.ROOT_APP_ID or os.environ.get('ROOT_APP_ID')
ROOT_APP_SECRET = settings.ROOT_APP_SECRET or os.environ.get('ROOT_APP_SECRET')


class RootException(Exception):
    pass


def list_gadget_models():
    result = requests.get("%s/gadgets/models" % BASE_URL, 
                          auth=HTTPBasicAuth(ROOT_APP_ID, 
                                             ROOT_APP_SECRET
                                             )
                          )
    if result.status_code == 200:
        return result.json()
    else:
        raise RootException()
