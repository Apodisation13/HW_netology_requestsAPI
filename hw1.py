import requests

token = 2619421814940190

# hulk = 332  # это я вначале нашёл их там просто в списке
# captain_america = 149
# thanos = 655

superheroes = ["Hulk", "Captain America", "Thanos"]
intelligence = []

for each in superheroes:
    url = f'https://superheroapi.com/api/{token}/search/{each}'
    response = requests.get(url)
    # each_id = response.json()['results'][0]['id']
    # print(each_id)
    each_intel = int(response.json()['results'][0]['powerstats']['intelligence'])
    # print(each_intel)
    intelligence.append(each_intel)

print(max(intelligence))
# Танос - id655, intelligence100
