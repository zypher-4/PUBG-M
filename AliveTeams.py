import requests
import json
from DataSet import Data

temp = []

url_team = f"http://192.168.0.174:10086/getteaminfolist"
r_team = requests.get(url_team)
data_team = r_team.json()

for i in data_team["teamInfoList"]:
    if i["liveMemberNum"] > 0:
        temp.append({
            "Name": Data.fill_team_names(i["teamId"]),
            "AlivePlayers": i["liveMemberNum"],
            "Kills": i["killNum"]
        })

with open("AliveTeams.txt", "w") as outfile:
    json.dump(temp, outfile)
