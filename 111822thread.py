import threading
import json
import requests


image_list = []
with open("sample_json.json", "r") as json_pics:
    pics = json.load(json_pics)
    for i in pics:
        image_list.append(pics[i])


def downloading(dict_):
    url = dict_["image-url"]
    name = dict_["name"]
    try:
        response = requests.get(url)
    except Exception as err:
        print(f"{err} ")
        return
    s_code = str(response.status_code)
    if s_code.startswith("2"):
        with open(f"{name}.jpeg", "wb") as picture:
            picture.write(response.content)
    print(f"{name} image is downloaded")

for i in range(len(image_list)):
    x = threading.Thread(target=downloading, args=(image_list[i],))
    x.start()
