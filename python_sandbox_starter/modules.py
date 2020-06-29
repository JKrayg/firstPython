# A module is basically a file containing a set of functions to include in your application.
# There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#Core modules
import datetime
today = datetime.date.today()

from datetime import date
today2 = date.today()

import time
timestamp = time.time()

from time import time
timestamp2 = time()

#Pip module
from camelcase import CamelCase
c = CamelCase()
print(c.hump("hello there world"))

#Import Custom module ---- validator.py
import validator
from validator import validate_email

email = "test@test.com"

if validate_email(email):
    print("Email is valid")
else:
    print("Email is bad")

