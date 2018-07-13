#!/usr/bin/env python

import os
import sys

os.system('clear')
message = '''Please enter your choice:
1) nth Fibonacci number
2) last Fibonacci number <= n
3) quit
'''
option = int(input(message))

if option == 1 or option == 2:
    number = int(input("\nPlease enter the number: "))
    # IMPLEMENT OPTIONS 1 AND 2 HERE
elif option == 3:
    os.system('clear')
    sys.exit()
else:
    print("I didn't understand your option")

input('\nPress enter to quit...')
os.system('clear')
