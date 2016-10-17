# Practice 4

import sys

def convertLower(s):

    result = s.lower() # convert to lower
        
    for i in range(len(result)):
        # if char is white space then delete it
        if (result[i]==" "):
            result = result.replace(s[i],'')

    print(result)
    return result

def blackOrWhite(col):

    col = convertLower(col) # convert string to lower case & remove any white space 
    
    if (col == "black" or col == "white"):
        return True  # ERROR HERE: true is not defined I thought it was in Python??
    else: return False

def main():

    colour = input("Please input a colour: ")

    if (blackOrWhite(colour)==True):
        print("The color was black or white")
    # else if colour's first character starts with the letter after 'k'
    elif (colour[0]==('k'+1) or colour[0]==('K'+1)):
        print("The color starts with a letter that comes after ""k"" in the alphabet")
        

main()
