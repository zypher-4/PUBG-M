import requests
import csv
from DataSet import Data

temp = []

url_player = "http://192.168.0.174:10086/gettotalplayerlist"
r_player = requests.get(url_player)
data_player = r_player.json()

for i in data_player["playerInfoList"]:
    temp.append({
        "Name": Data.fill_player_names(i["uId"]),
        "Kills": i["killNum"],
        "Assists": i["assists"],
        "Damage": i["damage"],
        "Max Kill Distance": i["maxKillDistance"],
        "Damage": i["damage"],
        "Damage Taken": i["inDamage"],
        "Headshots": i["headShotNum"],
        "Survival Time": i["survivalTime"],
        "Drive Distance": i["driveDistance"],
        "March Distance": i["marchDistance"],
        "Kills By Grenade": i["killNumByGrenade"],
        "Time Outside Zone": i["outsideBlueCircleTime"],
        "Knockouts": i["knockouts"]
    })

keys = temp[0].keys()

with open("PlayerStats.csv", "w", newline="") as outfile:
    dict_writer = csv.DictWriter(outfile, restval="-", fieldnames=keys, delimiter=',')
    dict_writer.writeheader()
    dict_writer.writerows(temp)
