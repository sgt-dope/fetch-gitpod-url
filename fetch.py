import requests
import os
from requests.auth import HTTPBasicAuth


get_url = requests.get(
    url="https://fetch-url-ff.herokuapp.com/",
    auth = HTTPBasicAuth(os.environ.get("AUTH_USERNAME"), os.environ.get("AUTH_PASSWORD"))
)

keycloak_url = get_url.json()[0]["url"]
print(keycloak_url)