import requests
import json
import csv
from DataSet import Data

temp = []

url_team = f'http://192.168.0.174:10086/getteaminfolist'
r_team = requests.get(url_team)
data_team = r_team.json()

url_player = f'http://192.168.0.174:10086/gettotalplayerlist'
r_player = requests.get(url_player)
data_player = r_player.json()


def scores():
    for j in data_team["teamInfoList"]:
        for i in data_player["playerInfoList"]:
            if i["teamId"] == j["teamId"]:
                total = Data.points_table(i["rank"]) + j["killNum"]
                temp.append({
                    "Id": Data.fill_team_names(i["teamId"]),
                    "Kills": j["killNum"],
                    "Rank": i["rank"],
                    "Placement Score": Data.points_table(i["rank"]),
                    "Total": total
                })
                break
    newlist = sorted(temp, key=lambda i: (i["Total"]), reverse=True)
    keys = newlist[0].keys()

    with open("ScoreBoard.csv", "w", newline="") as outfile:
        dict_writer = csv.DictWriter(outfile, restval="-", fieldnames=keys, delimiter=',')
        dict_writer.writeheader()
        dict_writer.writerows(newlist)
        # dict_writer.writerow({})


for i in data_player["playerInfoList"]:
    if i["rank"] == 1:
        scores()
        exit()
