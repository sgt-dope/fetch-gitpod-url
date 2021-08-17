import requests

get_url = requests.get(
    url="https://fetch-url-ff.herokuapp.com"
)

keycloak_url = get_url.json()[0]["url"]
print(keycloak_url)