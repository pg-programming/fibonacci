#!/usr/bin/env python

import sys

os.system('clear')
option = int(raw_input('Please enter your choice:\n1) nth Fibonacci number\n2) last Fibonacci number <= n\n3) quit\n'))

if option == 1 or option == 2:
    number = int(raw_input("\nPlease enter the number: "))
    # IMPLEMENT OPTIONS 1 AND 2 HERE
elif option == 3:
    os.system('clear')
    sys.exit()
else:
    print "I didn't understand your option"

raw_input('\nPress enter to quit...')
os.system('clear')
