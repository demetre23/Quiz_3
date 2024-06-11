# import requests
# import json
# import sqlite3
# f1 = "f1.sqlt"
# connection = sqlite3.connect(f1)
# c = connection.cursor()
#
#
# url = "https://api-formula-1.p.rapidapi.com/rankings/races"
#
# querystring = {"race":"50"}
#
# headers = {
# 	"x-rapidapi-key": "8b768a0b53mshb73968dfa1d4bc2p1e04d3jsn7a2169c91da6",
# 	"x-rapidapi-host": "api-formula-1.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
# # print(response.status_code)
# # print(response.text)
# # print(response.headers)
# content = response.json()
# # print(content)
#
# drivers_name = content['response'][0]['driver']['name']
# drivers_number = content['response'][0]['driver']['number']
# team_name = content['response'][1]['team']['name']
#
# # c.execute('''CREATE TABLE IF NOT EXISTS f1
# #              (Driver TEXT, Team TEXT,
# #              Number INTEGER,
# #              ID INTEGER PRIMARY KEY AUTOINCREMENT )''')
#
# c.execute("INSERT INTO f1 ('Driver', 'Team', Number) VALUES (?,?,?)", (drivers_name, team_name, drivers_number))
# connection.commit()























