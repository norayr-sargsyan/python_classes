import requests
import json


class Pictures:

    def __init__(self, json_with_pics):
        self.pics = json_with_pics
        self.image_list = []

    def image_in_json(self):
        with open(self.pics, "r") as pics_:
            fine = json.load(pics_)

            for item in fine:
                for i in item:
                    if i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png"):
                        self.image_list.append(i)
            return self.image_list

    def jpeg_download(self, name):
        for url in self.image_list:
            if url.endswith(".jpeg"):
                try:
                    response = requests.get(url)
                except Exception as err:
                    print(f"{err}")
                    return

                s_code = str(response.status_code)
                if s_code.startswith("2"):
                    with open(f"{name}.jpeg", "wb") as pics:
                        pics.write(response.content)

    def png_download(self, name):
        for url in self.image_list:
            if url.endswith(".png"):
                try:
                    response = requests.get(url)
                except Exception as err:
                    print(f"{err}")
                    return

                s_code = str(response.status_code)
                if s_code.startswith("2"):
                    with open(f"{name}.png", "wb") as pics:
                        pics.write(response.content)


picture = Pictures(json_with_pics="sample_json.json")
print(picture.image_in_json(), picture.png_download(name="new_png"), picture.jpeg_download(name="new_jpeg"))
