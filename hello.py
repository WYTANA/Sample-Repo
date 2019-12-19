# import math
# import os
# import sys

import requests

# print(sys.version)
# print(sys.executable)

# print("Hello World!")

r = requests.get("https://www.nhl.com/")
print(r.status_code)
print(r.ok)
# print("I am learning")
# name = input("Your name? ")
# print("Hello,", name, "!!")
