'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # check for count of instances of "th" in the single "word" argument
    #
    
    # base case
    # if length of word is less than 2 it cannot equal "th"
    if len(word) < 2:
        return 0
    
    # check if first two letters equal "th"
        # if so return 1 and make recursive call to 
        # check the next two characters (slice off first letter)
    elif word[0:2] == "th":
        return 1 + count_th(word[1:])
    # else the first two letter do not equal "th"
        # make recursive call to check the next two characters 
        # (slice off first letter of current version of word)
    else:        
        return count_th(word[1:])
        
