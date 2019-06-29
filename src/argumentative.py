#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from sys import argv


if len(argv) < 4:
    print(f'Usage: python argumentative.py [USER] [TASK] [BENEFIT]')
else: 
    user = argv[1]
    task = argv[2]
    benefit = argv[3]
    print(f'As a {user} I want to {task} so that {benefit}')