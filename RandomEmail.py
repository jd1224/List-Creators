import requests
from csv import reader
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', help='Number of emails to produce',
                    type=int, required=True)
args = parser.parse_args()

first_names = []
last_names = []
domains = []
normal_domains = []
nicknames = []

with open('firstnames.txt', 'r') as infile:
    first_names = infile.readlines()

with open('lastnames.txt', 'r') as infile:
    last_names = infile.readlines()

with open('nicknames.txt', 'r') as infile:
    nicknames = infile.readlines()

with open('states.csv', 'r') as infile:
    csv_reader = reader(infile)
    states = list(csv_reader)

with open('domains.txt', 'r') as infile:
    domains = infile.readlines()

with open('normaldomains.txt', 'r') as infile:
    normal_domains = infile.readlines()

def make_email(type):
    email =''
    first = ''
    domain = ''
    if type == 'name':
        seperators = ['.', '-', '']
        seperator = random.choice(seperators)
        if random.randint(1,100)>15:
            random_ender = str(random.randint(1,10000))
        else:
            random_ender = ''
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        first = f'{first_name.rstrip()}{seperator.rstrip()}{last_name.rstrip()}{random_ender.rstrip()}'
    
    elif type == 'nickname':
        first = random.choice(nicknames).rstrip()
        if random.randint(1,100)>15:
            random_ender = str(random.randint(1,10000))
        else:
            random_ender = ''
        first += random_ender
    
    if random.randint(1,100)<25:
        domain = random.choice(domains).rstrip()
    else:
        domain = random.choice(normal_domains).rstrip()
    
    third = [first, domain]
    email = '@'.join(third)
    return(email)

for i in range(1,args.n):
    choices = ['name', 'nickname']

    print(make_email(random.choice(choices)))