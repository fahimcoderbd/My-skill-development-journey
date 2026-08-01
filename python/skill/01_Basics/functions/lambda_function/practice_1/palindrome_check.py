def palindrome_check(data):
    if not data:
        return None
    
    is_palindrome = lambda s: True if s == s[::-1] else False

    return is_palindrome(data)

#testing
print(palindrome_check("madam"))
print(palindrome_check("python"))