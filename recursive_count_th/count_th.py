'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    str2 = 'th'
    n2 = len(str2)
    n1 = len(word)
     
    # return not (word == 'TH') and ord(word[0]) >=  65 and ord(word[0]) <= 90

    # def count(word,  n=len(word)):
    #     # n=len(word)
    
    #     if n == 1:
    #         return count_th(word[0])
    
    #     return count(word, n-1) + count_th(word[n-1])

    if word == 0 or n1 < n2 :
        return 0
    elif word[0: n2] == str2:
        return 1 + count_th(word[n2 - 1:])
    else:
        return count_th(word[n2 - 1:])
    
