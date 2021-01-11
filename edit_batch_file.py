import requests
import random

COMMANDS = """
@echo off
cd C:\\GayApe
gay_ape.exe
"""

enabled = requests.get('https://raw.githubusercontent.com/CalebWebsterJCU/GayApe/master/enabled.txt')
enabled.raise_for_status()

if enabled.text == 'True':
    chances = requests.get('https://raw.githubusercontent.com/CalebWebsterJCU/GayApe/master/chances.txt')
    chances.raise_for_status()
    rand_num = int(chances.text)  # Odds of Gay Ape running, e.g. 10 = 1 in 10 chance
    if random.randint(1, rand_num) == 1:
        # Write commands to batch file
        with open('C:\\GayApe\\run_gay_ape.bat', 'w') as batch_file:
            print(COMMANDS, file=batch_file)
else:
    # Erase batch file
    with open('C:\\GayApe\\run_gay_ape.bat', 'w') as batch_file:
        print('', file=batch_file)
