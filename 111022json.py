import json
import yaml
from yaml import Loader


users = []
check = True
while check:
    input_ = input("name surname ")
    dict_ = dict(
        name=input_.split()[0],
        surname=input_.split()[1]
    )
    users.append(dict_)
    input_2 = input("for exit write yes ")
    if input_2.lower() == "yes":
        check = False

with open("users.json", "a") as json1:
    json.dump(users, json1, indent=3)
# 1

with open("users.json", "r") as json2:
    users_list = json.load(json2)

with open("json_to.txt", "a") as txt1:
    for i in range(len(users_list)):
        txt1.write(f"{i + 1}: {users_list[i]}\n")
# 2

with open("yaml_from_json.yml", "a") as yaml1:
    yaml.dump(users_list, yaml1)

# 3

with open("yaml_from_json.yml", "r") as yaml2:
    new_list = yaml.load(yaml2, Loader=Loader)

with open("yaml_to_json.json", "a") as json3:
    json.dump(new_list, json3, indent=4)

# 4

with open("yaml_to.txt", "a") as txt2:
    for item in range(len(new_list)):
        txt2.write(f"{item + 1}: {new_list[item]}\n")
