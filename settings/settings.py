# Global Settings for project rather than env vars
# Leave variables empty if you want to use env variables
from base64 import b64encode
import base64
SANDBOX = True

SANDBOX_URL = "https://sandbox.root.co.za/v1/insurance"
PROD_URL = "https://api.root.co.za/v1/insurance"

BASE_URL = SANDBOX_URL if SANDBOX else PROD_URL

API_KEY = "__Replace__"
API_ID = "__Replace__"

ROOT_APP_SECRET = "" if SANDBOX else API_KEY
ROOT_APP_ID = API_KEY if SANDBOX else API_ID
