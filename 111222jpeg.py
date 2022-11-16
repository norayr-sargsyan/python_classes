import requests
import json


class Pictures:
    image_list = []

    def __init__(self, json_with_pics):
        self.pics = json_with_pics

    def image_in_json(self):
        with open(self.pics, "r") as pictures:
            fine = json.load(pictures)
        for i in fine:
            if fine[i].endswith("jpg") or fine[i].endswith("jpeg") or fine[i].endswith("png"):
                self.image_list.append(fine[i])
        return self.image_list

    def jpeg_download(self, name):
        for url in self.image_list:
            if url.endswith("jpeg"):
                try:
                    response = requests.get(url)
                except Exception as err:
                    print(f"{err}")
                    return

                s_code = str(response.status_code)
                if s_code.startswith("2"):
                    with open(f"{name}.jpeg", "wb") as pics:
                        pics.write(response.content)
        return f"Done: {name} is downloaded"

    def png_download(self, name):
        for url in self.image_list:
            if url.endswith("png"):
                try:
                    response = requests.get(url)
                except Exception as err:
                    print(f"{err}")
                    return

                s_code = str(response.status_code)
                if s_code.startswith("2"):
                    with open(f"{name}.png", "wb") as pics:
                        pics.write(response.content)

        return f"Done: {name} is downloaded"


picture = Pictures("sample_json.json")
print(picture.image_in_json(), picture.png_download(name="new_png"), picture.jpeg_download(name="new_jpeg"))
