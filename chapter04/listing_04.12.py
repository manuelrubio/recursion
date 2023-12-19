def is_palindrome(s):
    n = len(s)
    if n <= 1:
        return True
    else:
        return (s[0] == s[n - 1]) and is_palindrome(s[1:n - 1])


# Test
print(is_palindrome(''))
print(is_palindrome('a'))
print(is_palindrome('ab'))
print(is_palindrome('aa'))
print(is_palindrome('aba'))
print(is_palindrome('cba'))
print(is_palindrome('abcba'))
print(is_palindrome('dbcba'))
print(is_palindrome('abcda'))
