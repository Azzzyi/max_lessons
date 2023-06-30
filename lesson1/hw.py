def is_polindrome(str):
    return str == str[::-1]

def is_polindrome2(str):
    for i in range(len(str)):
        if(str[i] != str[-i - 1]):
            return False
    return True


"""
print(is_polindrome(""))
print(is_polindrome("N"))
print(is_polindrome("arozaupalanalapuazora"))
"""
print(is_polindrome2("adhfskjansdfjk"))