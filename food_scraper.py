import csv 
import requests 

URL = "https://api.nal.usda.gov/ndb/list?format=json&lt=f&sort=n&api_key=hpkfP0VHXl4eeOLlOL9QLPcxK6hOv2A6lJ7pYUnr"

def get_data():
  r = requests.get(URL)
  r = r.json()
  # RESULTS = {'children': []}
  # for line in csv.DictReader(data.splitlines(), skipinitialspace=True):
  #   RESULTS['children'].append({
  #     'name': line['Name'],
  #   })
  return r