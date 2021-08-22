import requests
import os
from requests.auth import HTTPBasicAuth


get_url = requests.get(
    url="https://fetch-urls-ff.herokuapp.com/",
    auth = HTTPBasicAuth(os.environ.get("AUTH_USERNAME"), os.environ.get("AUTH_PASSWORD"))
)

kc_url = get_url.json()[0]["urls"]["keycloak_url"]
app_url = get_url.json()[0]["urls"]["app_url"]

print(f"Keycloak URL is: {kc_url}\nApp URL is: {app_url}")