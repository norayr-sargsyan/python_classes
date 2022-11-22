import threading
import json
import requests
from multiprocessing import Pool


class Downloader:
    def __init__(self, json_file):
        self.image_list = []
        with open(json_file) as json_pics:
            pics = json.load(json_pics)
            for i in pics:
                self.image_list.append(pics[i])

    def img_downloading(self, url, name):
        print("started", name)
        try:
            response_ = requests.get(url)
        except Exception as err:
            print(f"{err}")
            return

        s_code = str(response_.status_code)
        if s_code.startswith("2"):
            with open(f"{name}", "wb") as photo:
                photo.write(response_.content)
                print(f"image {name} is downloaded")

    def td_download(self):
        new_list = []
        for item in self.image_list:
            x = threading.Thread(target=self.img_downloading, args=(item["name"], item["image-url"]))
            new_list.append(x)
            x.start()
        for img in new_list:
            img.join()
        print("Done: all images is downloaded")
