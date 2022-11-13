from datetime import datetime
from copy import deepcopy
import requests
import json
import yaml
from yaml import Loader
dict_ = dict(
    year=datetime.now().year,
    month=datetime.now().month,
    day=datetime.now().day
)

with open("sample_json.json", "w") as fd:
    json.dump(dict_, fd, indent=4)

from yaml import Loader
# with open("sample_yaml.yml", "r") as yml_file:
#     data_ = yaml.safe_load(yml_file)
#
# with open("new_json.json", "w") as new_one:
#     json.dump(data_, new_one, indent=4)
