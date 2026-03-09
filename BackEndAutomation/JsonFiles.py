import json

with open('C:\\Temp\\sample.json') as f:
    data = json.load(f)
    #print(data)
    one = data['users'][0]
    print(one['name'])

print(type(data))
