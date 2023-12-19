def longest_palindrome_substring(s):
    n = len(s)
    if is_palindrome(s):
        return s
    else:
        s_aux_1 = longest_palindrome_substring(s[1:n])
        s_aux_2 = longest_palindrome_substring(s[0:n - 1])
        if len(s_aux_1) > len(s_aux_2):
            return s_aux_1
        else:
            return s_aux_2


# Test
def is_palindrome(s):
    n = len(s)
    if n <= 1:
        return True
    else:
        return (s[0] == s[n - 1]) and is_palindrome(s[1:n - 1])


print(longest_palindrome_substring(''))
print(longest_palindrome_substring('a'))
print(longest_palindrome_substring('ab'))
print(longest_palindrome_substring('aa'))
print(longest_palindrome_substring('aba'))
print(longest_palindrome_substring('abaa'))
print(longest_palindrome_substring('abaab'))
print(longest_palindrome_substring('ACGTGTACCATCCG'))
