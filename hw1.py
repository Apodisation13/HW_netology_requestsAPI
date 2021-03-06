import requests

token = 2619421814940190

# hulk = 332
# captain_america = 149
# thanos = 655

superheroes = ["Hulk", "Captain America", "Thanos"]
intelligence = []

for each in superheroes:
    url_id = f'https://superheroapi.com/api/{token}/search/{each}'
    responce_id = requests.get(url_id)
    each_id = responce_id.json()['results'][0]['id']
    url_intel = f'https://superheroapi.com/api/{token}/{each_id}/powerstats'
    responce_intel = requests.get(url_intel)
    print(responce_intel.json())
    each_intel = int(responce_intel.json()['intelligence'])
    print(each_intel)
    intelligence.append(each_intel)

print(intelligence)
