def length_longest_palindrome_subseq(a):
    n = len(a)
    if n <= 1:
        return n
    else:
        if a[0] == a[n - 1]:
            return 2 + length_longest_palindrome_subseq(
                a[1:n - 1])
        else:
            l1 = length_longest_palindrome_subseq(a[1:n])
            l2 = length_longest_palindrome_subseq(a[0:n - 1])
            return max(l1, l2)
