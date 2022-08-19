# 111.733.638-4
from pyperclip import copy
from sys import argv
copy("".join(v for v in argv[1] if v.isalnum()))
