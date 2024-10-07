s = input("Enter a string: ")

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

if is_palindrome(s):
    print(True)
else:
    print(False)
