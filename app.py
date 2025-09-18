import requests
import json
import statsapi
import mlbstatsapi

mlb = mlbstatsapi.Mlb()

# Example: Get Dodgers roster
#wow = statsapi.get("sports_players")['season']


#url = "http://statsapi.mlb.com/api/v1/"
#response = requests.get(url)
#ata = response.json()
#rint(json.dumps(data, indent=4))

#stats = ['expectedStatistics']
#groups = ['hitting']
#arams = {'season': 2022}

#def getId(name):
#    return mlb.get_people_id(name)[0]

#print(wow)
#print(dir(mlb))
#mmm = mlb.get_player_stats(getId("Mike Trout"), stats=stats, groups=groups, **params)
#mmm2 = mmm['expectedStatistics']['season']
#for split in mmm2.splits:
#     for k, v in split.stat.__dict__.items():
#            print(k, v)

player_id = mlb.get_people_id('Ty France')[0]

stats = ['expectedStatistics']
group = ['hitting']
params = {'season': 2022}

stats = mlb.get_player_stats(player_id, stats=stats, groups=group, **params)
expectedstats = stats['hitting']['expectedstatistics']
for split in expectedstats.splits:
    for k, v in split.stat.__dict__.items():
        print(k, v)



#print(data)

#roster = data["roster"]


#for x in data:
    #name = player["person"]["fullName"]
    #jersey = player.get("jerseyNumber", "N/A")
    #position = player["position"]["name"]
    #status = player["status"]["description"]
    #print(f"{name:<20} | #{jersey:<3} | {position:<15} | {status}")
    #print(x)
