# encoding: utf-8
"""
Gruenkohl Alarm
"""

# imports
import requests
import json
from urllib2 import urlopen
import unidecode
import datetime

#For Monday
def monday():
  today = datetime.datetime.today().weekday()
  if today == 0:
    for x in range(4):
      apiRequest = "https://api.mensa.legacymo.de/" + str(x)
      response = urlopen(apiRequest)
      string = response.read().decode('utf-8')
      json_obj = json.loads(string)
      day = json_obj['day']
      date = json_obj['date']
      essen1 = json_obj['food'][0]
      #print(essen1)
      meal = essen1['meal']
      #print(meal)
      name = meal[0]
      #print(name)
      name_string = name['name']
      #print(name_string)

      if u"Bremer Grünkohl mit Kasseler & Salzkartoffeln" in name_string:
        print(u"There will be Grünkohl on (" + day + ", " + date + ")")
        requests.get("bot<token>/METHOD_NAME" + "Diesen " + day + ", den " + date + u" gibt es Grünkohl " +  u"\U0001F389")


#For Tomorrow
def tomorrow():
  response = urlopen("https://api.mensa.legacymo.de/1")
  string = response.read().decode('utf-8')

  json_obj = json.loads(string)
  day = json_obj['day']
  date = json_obj['date']
  essen1 = json_obj['food'][0]
  #print(essen1)
  meal = essen1['meal']
  #print(meal)
  name = meal[0]
  #print(name)
  name_string = name['name']
  #print(name_string)

  if u"Bremer Grünkohl mit Kasseler & Salzkartoffeln" in name_string:
    #bot token: 746180339:AAFUwKyUohGWcsomj2trzHVLeP2VfPXNb78
    #chat id: -312656574
    #print("true")
    print(u"There will be Grünkohl on (" + day + ", " + date + ")")
    requests.get("bot<token>/METHOD_NAME" + u"\U0000261D" + u"Morgen gibt's Grünkohl! (" + day + ", " + date + ")" + "'")

#For today
def today():
  response = urlopen("https://api.mensa.legacymo.de/0")
  string = response.read().decode('utf-8')

  json_obj = json.loads(string)
  day = json_obj['day']
  date = json_obj['date']
  essen1 = json_obj['food'][0]
  #print(essen1)
  meal = essen1['meal']
  #print(meal)
  name = meal[0]
  #print(name)
  name_string = name['name']
  #print(name_string)

  if u"Bremer Grünkohl mit Kasseler & Salzkartoffeln" in name_string:
    #print("There will be Gr&uumlnkohl today! (" + day + ", " + date + ")")
    #bot token: 746180339:AAFUwKyUohGWcsomj2trzHVLeP2VfPXNb78
    #chat id: -312656574
    print(u"There will be Grünkohl on (" + day + ", " + date + ")")
    requests.get("bot<token>/METHOD_NAME" + u"\U0001F389" + u"Heute gibt's Grünkohl! (" + day + ", " + date + ")" + "'")

monday();
tomorrow();
today();

