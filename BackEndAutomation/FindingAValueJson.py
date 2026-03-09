import json
data = {}
key ='Bob'
ans=''
with open('C:\\Temp\\sample.json') as j:
    data = json.load(j)
    for i in data['users']:
        if key == i['name']:
            ans = i['id']
print(ans)
