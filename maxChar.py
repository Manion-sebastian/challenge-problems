# Directions:

# Given a string, return the character that is most commonly used in the string.

# Examples:

# maxChar("abcccccccd") === "c"
# maxChar("apple 1231111") === "1"



def maxChar(nput):

    charVault = {}
    for x in nput:
        if x in charVault:
            charVault[x] += 1
        else:
            charVault[x] = 1

    max_occ = max(charVault, key = charVault.get)

    print(f'the most occuring character in {nput} is {max_occ}') 


maxChar('brandon')


