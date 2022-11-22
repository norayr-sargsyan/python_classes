from random import randint
import requests


def password_gen():
    while True:
        yield f"{chr(randint(97, 122))}{chr(randint(65, 90))}{chr(randint(97, 122))}{randint(0, 9)}{chr(randint(97, 122))}" \
              f"{randint(0, 9)}{chr(randint(97, 122))}{randint(0, 9)}"


def citation_gen():
    while True:
        try:
            cit_ = requests.get("https://zenquotes.io/api/random").json()
        except Exception as err:
            print("<<<<ERROR>>>>", "check a connection", f"{err}", sep="\n")
            return
        yield f"<<{cit_[0]['q']}>> --{cit_[0]['a']}"


