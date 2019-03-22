import csv 
import requests 
import json 

URL = "https://api.nal.usda.gov/ndb/search/?format=json&q=butter&ds=SR&sort=r&max=5&offset=0&api_key=hpkfP0VHXl4eeOLlOL9QLPcxK6hOv2A6lJ7pYUnr"
# "https://api.nal.usda.gov/ndb/reports/?ndbno=01009&type=b&format=json&api_key=hpkfP0VHXl4eeOLlOL9QLPcxK6hOv2A6lJ7pYUnr"
# "https://api.nal.usda.gov/ndb/nutrients/?format=json&api_key=hpkfP0VHXl4eeOLlOL9QLPcxK6hOv2A6lJ7pYUnr&nutrients=307&nutrients=203&nutrients=205&nutrients=204&nutrients=208&nutrients=269&ndbno=01009"
# "https://api.nal.usda.gov/ndb/list?format=json&lt=nr&sort=n&max=500&api_key=hpkfP0VHXl4eeOLlOL9QLPcxK6hOv2A6lJ7pYUnr"


# calories 
# protein -> 203
# carbohydrates -> 205 
# total fat -> saturated/unsaturated -> 204 for total, unsat = 645 + 646, sat = 606
# cholesterol -> 601
# sugar -> 269 (total)
# fiber -> 291 
# calcium -> 301
# sodium -> 307 
# potassium -> 306
# caffeine -> 262 

def get_data(food):
  URL = 'https://api.nal.usda.gov/ndb/search/?format=json&q=' + food + '&sort=r&max=10&offset=0&api_key=hpkfP0VHXl4eeOLlOL9QLPcxK6hOv2A6lJ7pYUnr'

  r = requests.get(URL)
  r = r.json()
  r = r["list"]["item"]
  print type(r)
  item = ""
  for i in range(len(r)):
    if r[i]["ds"] == "SR":
      item = r[i] 
  print type(item)
  food_num = item["ndbno"]

  URLL = "https://api.nal.usda.gov/ndb/nutrients/?format=json&api_key=hpkfP0VHXl4eeOLlOL9QLPcxK6hOv2A6lJ7pYUnr&nutrients=307&nutrients=203&nutrients=205&nutrients=204&nutrients=208&nutrients=269&ndbno=" + food_num

  new_r = requests.get(URLL)
  new_r = new_r.json()
  return new_r
