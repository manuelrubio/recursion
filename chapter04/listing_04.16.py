def pascal(n):
    if n == 0:
        return [1]
    else:
        row = [1]
        previous_row = pascal(n - 1)
        for i in range(len(previous_row) - 1):
            row.append(previous_row[i] + previous_row[i + 1])
        row.append(1)
    return row


# Test
for n in range(0, 6):
    print(pascal(n))
