import sys
import os
PATH = r"C:\Users\sbferreira\OneDrive\BKP SECRETARIA"
# arg = sys.argv[1]


def newdir(d): return os.path.join(PATH, d)


# print(newdir("teste tarefa"))
# os.mkdir(newdir("teste tarefa"))
from prime_nums import get_prime_nums, is_prime

is_prime(151)