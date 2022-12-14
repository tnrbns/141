# Rubinos, Tyna S.
# BSCS II
# MP3 - Smiling is Not a Regular Expression
# Given a regular expression, determine whether certain strings are generated by it.
# Special thanks to W3Schools.com for the quick regex crash course in Python, regex101.com for double checking my regular expressions

# Regular expression module
import re 

# Converts user regex input to Python-readable regex
def regexConverter(str_regex):
    # Empty string = e
        # Use Kleene plus instead of star
    # aaa* = ^aaa*$ 
    # (ab)* = ^e|(ab)+$
    # a*b* = ^e|a*b*$
    # a+b = ^a|b$
    # (ab)*(aa+bb) = ^(ab)*(aa|bb)$

    new_regex = str_regex

    if re.search(".+\+.+",str_regex):
        # Replace '+' character OR to '|' character
        new_regex = new_regex.replace("+","|")
    elif re.search(".+\)\*$", str_regex):
        # Add 'e|' to represent empty string
        new_regex = ("e|"+str_regex)
        # Replace first '*' to '+' (Since 'e' now represents the empty string)
        new_regex = new_regex.replace("*", "+", 1)

    # Add '^' at beginning and '$' at end for concatenation (for regex (ab)*, 'ab' is VALID while 'ba' is INVALID) 
    new_regex = ("^"+new_regex+"$")

    # Remove spaces 
    new_regex = new_regex.replace(" ", "")
    
    return new_regex

# Checks whether string is viable in the regular expression     
def regexChecker(str_input,str_regex):
    if re.search(str_regex,str_input): return "yes"
    else: return "no"

# No. of test cases
x = int(input("No. of test cases: "))

# Create list to store outputs
out_list = []

for i in range(x):
    # Print each regex
    j = 1
    while j == 1:
        input_regex = input("Input regular expression: ")
        
        # Invalid regex: ((ab)(ba)*)*, ((aba)*(bab)*)*, (a+b)* or (ab+ba)*
        # Some notes so it doesn't get confusing:
        # \(\(.+\)\*.*\)\* = checks if input contains two instances of ')*'
            # '\(\(' to check if regular expression begins with two parentheses (indicating it's "starred" in a group)
                # (ab)*(ab)* must be VALID
            # .+ means one or more characters before the first ')*' (e.g (ab)*)
            # .* means zero or more characters before the second ')*' 
                # ((ab)*)* or ((ab)*b)* must be INVALID
            # \(, \) and \* = characters to check
        # | = or
        # .+\+.+\)\* = checks if input contains union character (+) enclosed in ')*'
        # \+, \), \* characters to check
        #[^(].* = means all characters are covered EXCEPT for '(' followed by any character after the '+' character
                # (ab)+(ab)* and (ab)*+(ab) must be VALID
        if re.search("(\(\(.+\)\*.*\)\*)|(.+\+[^(].*\)\*)", input_regex): 
            print("Regular expression is not within scope. Try again.\n")
        else: 
            j = 0            

    input_regex = regexConverter(input_regex) 
    no_strings = int(input("Input no. of strings: "))

    for i in range(no_strings):
        check_str = input("Input string: ")

        # Function to check if string is accepted
        to_convert = regexChecker(check_str,input_regex)

        # Put output in list
        out_list.append(to_convert)

    # Print list
    str_outs = '\n'.join(out_list)
    print("\n"+str_outs+"\n")

    # Empty list
    out_list.clear()