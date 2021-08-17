import requests

get_url = requests.get(
    url="https://fetch-url-ff.herokuapp.com"
)

keycloak_url = get_url.json()[0]["url"]
print(keycloak_url)

#8809fb6b62173ff3c701d1fe9c52359d7895b58d9bfd036a