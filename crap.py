from os import rename

import requests


print("Hey, Mikey Bee")


def greet(who_to_greet):
    # test = 'foo'
    greeting = "HelloM. {}".format(who_to_greet)
    return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)
