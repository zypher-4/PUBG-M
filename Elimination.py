import requests
import json
from DataSet import Data

temp_rank = 25
url_player = f'http://192.168.0.174:10086/gettotalplayerlist'
r_player = requests.get(url_player)
data_player = r_player.json()

for i in data_player["playerInfoList"]:
    if i["rank"] == 1:
        break
    if i["rank"] > 0 and i["rank"] < temp_rank:
        temp_rank = i["rank"]
        j = i

try:
    if j["teamId"]:
        temp = Data.fill_team_names(j["teamId"])
        with open("Eliminitaion.txt", "w") as outfile:
            json.dump(temp, outfile)
except:
    pass
