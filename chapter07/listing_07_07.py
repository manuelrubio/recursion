def longest_palindrome_substring_alt(s):
    n = len(s)
    if n <= 1:
        return s
    else:
        s_aux_1 = longest_palindrome_substring_alt(s[1:n - 1])
        if len(s_aux_1) == n - 2 and s[0] == s[n - 1]:
            return s
        else:
            s_aux_2 = longest_palindrome_substring_alt(s[1:n])
            s_aux_3 = longest_palindrome_substring_alt(
                s[0:n - 1])
            if len(s_aux_2) > len(s_aux_3):
                return s_aux_2
            else:
                return s_aux_3


# Test
def is_palindrome(s):
    n = len(s)
    if n <= 1:
        return True
    else:
        return (s[0] == s[n - 1]) and is_palindrome(s[1:n - 1])


print(longest_palindrome_substring_alt(''))
print(longest_palindrome_substring_alt('a'))
print(longest_palindrome_substring_alt('ab'))
print(longest_palindrome_substring_alt('aa'))
print(longest_palindrome_substring_alt('aba'))
print(longest_palindrome_substring_alt('abaa'))
print(longest_palindrome_substring_alt('abaab'))
print(longest_palindrome_substring_alt('ACGTGTACCATCCG'))
