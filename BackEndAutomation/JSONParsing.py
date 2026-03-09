import json

courses = '{"name": "Rahul", "languages": ["Java", "python"]}'

#Loads method parses json string and it returns dictionary

dictionary_form = json.loads(courses)
print(dictionary_form)
print(type(dictionary_form))

print(dictionary_form["name"])
print(dictionary_form["languages"])
print(dictionary_form["languages"][0])
print(dictionary_form["languages"][1])

