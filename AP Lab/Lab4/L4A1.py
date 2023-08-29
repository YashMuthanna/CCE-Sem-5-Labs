def rev(text):
    return text[::-1]

def palindrome(text):
    if(text == rev(text)):
        return True
    return False

t = input("Enter text: ")
print(palindrome(t))
