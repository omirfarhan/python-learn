import json

person = {"name":"John","age":30,"city":"New York","hasChildren":False,"titles":["engineer","programmer"]}
person_json = json.dumps(person,indent = 2,sort_keys=True)

with open('person.json', 'r') as file:
    person_jsons=json.load(file)


print(person_jsons)

# # Convert the Python object to a JSON string
# person_json = json.dumps(person,indent = 2,sort_keys=True)
# print(person_json)

# # with open('person.json', 'w') as file:
# #     json.dump(person,file, indent = 2)

