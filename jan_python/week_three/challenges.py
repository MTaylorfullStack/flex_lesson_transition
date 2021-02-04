## Acronym
# Given a string, return an acronym containing the first letter of every word in the string.
# "Will you answer the door?" --> returns "Wyatd"

## declare a function, accept a string as a parameter
    ## store the first letter
    ## loop through the string
        ## if current value is a space
            ## add next string value to acronym
    ## return acronym

def generate_acronym(long_string):
    acronym=long_string[0]
    for i in range(len(long_string)):
        if long_string[i] == " ":
            acronym+=long_string[i+1]
    return acronym


# print(generate_acronym("Welcome To Python"))
# print(generate_acronym("Object Oriented Programming"))
# print(generate_acronym("Application Programming Interface"))


## Parentheses Valid
# Given a string, test whether parentheses inside of the string are valid.
# "he(llo)()" --> returns True, opening parentheses have corresponding closing parentheses
# "goodb(ye)(" --> returns False, opening parenthese is missing closing parenthese
# "hell)(ogood(bye)" --> returns False, closing parenthese comes before opening

## declare my function, given a string
    ## declare a close count
    ## declare an open count
    ## loop through the string
        ## if open paren
            ## count open
        ## if close paren
            ## count close
        ## if close > open
            ## return False
    ## if count open == count close
        ## return True
    ## return False

def parens_valid(par_string):
    open_count=0
    close_count=0
    for letter in par_string:
        if letter == "(":
            open_count+=1
        elif letter == ")":
            close_count+=1
        if close_count > open_count:
            return False
    if open_count == close_count:
        return True
    return False

print(parens_valid("goodb)()()()("))

