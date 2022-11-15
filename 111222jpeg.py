import requests
import os
import json


class Pictures:

    def __init__(self, json_with_pics):
        self.pics = json_with_pics
        self.image_list = []

    def image_in_json(self):
        for item in self.pics:
            for i in item:
                if i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png"):
                    self.image_list.append(i)
        return self.image_list

    def jpeg_download(self):
        sample = 0
        for i in self.image_list:
            sample += 1
            if i.endswith(".jpeg"):
                with open(f"new_pics{sample}.jpeg" "wb") as pics:
                    pics.write(i.content)

    def png_download(self):
        sample = 0
        for i in self.image_list:
            sample += 1
            if i.endswith(".png"):
                with open(f"new_pics{sample}.png" "wb") as pics:
                    pics.write(i.content)
