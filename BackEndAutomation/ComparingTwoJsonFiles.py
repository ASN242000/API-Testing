import json

with open('C:\\Temp\\sample.json') as f:
    dict1 = json.load(f)

with open('C:\\Temp\\sampleone.json') as f2:
    dict2 = json.load(f2)

print(dict1==dict2)