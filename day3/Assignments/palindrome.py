def reverse(s):
    return s[::-1]

def is_palindrome(s):
    rev_string = reverse(s)
    if (s == rev_string):
        return(True)
    return(False)

s = "hello"
answer = is_palindrome(s)

if answer == 1:
    print("The word",s, "is a palindrome")
else:
    print("The word",s, "is not a palindrome")
