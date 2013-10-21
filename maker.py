import random
import re
first_names_m = []
first_names_f = []
last_names = []
birthday_hash = {}

#with open("BIRTHDAY_HIST", "r") as f_in:

with open("SURNAMES", "r") as f_in:
    last_names = [[float(d) if d[0].isdigit() else d
                   for d in re.split('\s+', row)[:3]] if row else None\
                   for row in f_in.read().split('\n')][:-1]
with open("FIRST_NAMES_M", "r") as f_in:
    first_names_m = [[float(d) if d[0].isdigit() else d
                   for d in re.split('\s+', row)[:3]] if row else None\
                  for row in f_in.read().split('\n')]
with open("FIRST_NAMES_F", "r") as f_in:
    first_names_f = [[float(d) if d[0].isdigit() else d
                   for d in re.split('\s+', row)[:3]] if row else None\
                  for row in f_in.read().split('\n')]

def choose_name(name_list):
    choice = random.random()*100
    for name, p, cum_p in name_list:
        if choice <= cum_p:
            return name

def generate_person():
    pass:w

