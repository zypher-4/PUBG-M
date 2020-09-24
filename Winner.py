import requests
import csv
from DataSet import Data

temp = []

url_team = "http://192.168.0.174:10086/getteaminfolist"
r_team = requests.get(url_team)
data_team = r_team.json()

url_player = "http://192.168.0.174:10086/gettotalplayerlist"
r_player = requests.get(url_player)
data_player = r_player.json()

for i in data_player["playerInfoList"]:
    if i["rank"] == 1:
        temp.append({
            "Name": Data.fill_player_names(i["uId"]),
            "Kills": i["killNum"],
            "Assists": i["assists"],
            "Damage": i["damage"]
        })

try:
    keys = temp[0].keys()

    with open("Winners.csv", "w", newline="") as outfile:
        dict_writer = csv.DictWriter(outfile, restval="-", fieldnames=keys, delimiter=',')
        dict_writer.writeheader()
        dict_writer.writerows(temp)
except:
    print("Something Went Wrong")
