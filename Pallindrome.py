# check if a string a pallindrome using recursive function.
# first check the length of the string
# if the length is zero or one it is pallindrome
# if more than that then check the endpoints excluding the elements already checked, if the end result matches then its a pallindrome

def isPallindrome(s=''):
    if len(s) < 2:
        print('It is a pallindrome')
        return True
    if s[0] != s[-1]:
        print('It is not a pallindrome')
        return False
    return isPallindrome(s[1:-1])

s = input('Enter a string to check for the pallindrome: ')
isPallindrome(s)