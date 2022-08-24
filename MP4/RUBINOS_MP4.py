# Rubinos, Tyna S.
# BSCS II
# MP4 - Grammar Nazi 2.0
# DFA Implementation of the Syntax Checker - checks whether input is valid C variable or function type
# Special thanks to W3Schools for numPy tutorial, Appdividend for float-integer array conversion, Regex101 for rechecking regular expressions
# and Shekher Pandey of Linux Hint for CSV to 2D array instructions 

# Some limitations of this exercise:
    # Only illegal variable names are primitive data types (and void for function declaration). 
    # C-specific keywords like 'else', 'if', 'return', etc. were not identified in the DFA
        # 1 int if = 68; and 1 char void; will be VALID
        # 1 double double; and 2 int char(); will be INVALID
    # Variable declarations allow for one character to be converted as a number. I have included them all, even if some are invalid.
        # 1 float check = '\'; and 1 char test = '''; will be VALID 

import re                               # Regular expression module for checking other letters 
import numpy as np                      # Using numPy to convert .csv to 2D array for DFA
file = open('dfa.csv', 'rb')
dfa_table = np.loadtxt(file,delimiter = ",")
dfa_table = dfa_table.astype(int)       # Convert array of floats to integers (for index checking)

# Converts string list to a specific value
def strtoValue(str_in):
    # Digits 0-9
    if(str_in=='0'): return 0
    elif(str_in=='1'): return 1
    elif(str_in=='2'): return 2
    elif(str_in=='3'): return 3
    elif(str_in=='4'): return 4
    elif(str_in=='5'): return 5
    elif(str_in=='6'): return 6
    elif(str_in=='7'): return 7
    elif(str_in=='8'): return 8
    elif(str_in=='9'): return 9

    # Lowercase letters (for data types)
    elif(str_in=='a'): return 10
    elif(str_in=='b'): return 11
    elif(str_in=='c'): return 12
    elif(str_in=='d'): return 13
    elif(str_in=='e'): return 14
    elif(str_in=='f'): return 15
    elif(str_in=='h'): return 16
    elif(str_in=='i'): return 17
    elif(str_in=='l'): return 18
    elif(str_in=='n'): return 19
    elif(str_in=='o'): return 20
    elif(str_in=='r'): return 21
    elif(str_in=='t'): return 22
    elif(str_in=='u'): return 23
    elif(str_in=='v'): return 24

    # Other letters that aren't data types
    elif(re.search("[gjkmpqswxyz]",str_in)): return 25;
    elif(re.search("[A-Z]",str_in)): return 26;

    # Special characters
    elif(str_in==' '): return 27
    elif(str_in=='.'): return 28
    elif(str_in==','): return 29
    elif(str_in==';'): return 30
    elif(str_in=='='): return 31
    elif(str_in=='\''): return 32
    elif(str_in=='('): return 33
    elif(str_in==')'): return 34
    elif(str_in=='_'): return 35

    # Other characters not specifically mentioned
    else: return 36

# No. of test cases
num_testcase = int(input("No. of test cases: "))

for i in range(num_testcase):
    input_dec = input("Input string: ")
    str_list = list(input_dec)                  # Converts strings into list/array
    dfa_state = 0                               # Start state set to 0

    # Checks the string by character
    for x in range(len(str_list)):  
        dfa_input = strtoValue(str_list[x])
        dfa_state = dfa_table[dfa_state][dfa_input]

    # Checks if declarations are valid
    if (dfa_state==52): 
        print("VALID VARIABLE DECLARATION")
    elif (dfa_state==150): 
        print("VALID FUNCTION DECLARATION")
    elif (dfa_state==151): 
        print("INVALID VARIABLE DECLARATION")
    elif (dfa_state==152): 
        print("INVALID FUNCTION DECLARATION")
    else: print("INVALID INPUT")
