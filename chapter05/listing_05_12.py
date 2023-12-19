def partition_Hoare(a, lower, upper):
    if upper >= 0:
        middle = (lower + upper) // 2
        pivot = a[middle]
        a[middle] = a[lower]
        a[lower] = pivot

        left = lower + 1
        right = upper

        finished = False
        while not finished:
            while left <= right and a[left] <= pivot:
                left = left + 1

            while a[right] > pivot:
                right = right - 1

            if left < right:
                aux = a[left]
                a[left] = a[right]
                a[right] = aux

            finished = left > right

        a[lower] = a[right]
        a[right] = pivot

        return right


# Test
a = [4, 6, 0, 3, 5, 7, 4, 5, 2, 1]
b = a.copy()
print(a)
pivot_index = partition_Hoare(a, 0, len(a) - 1)
print('Pivot index = ', pivot_index,
      ', Pivot = ', b[pivot_index], sep='')
print(a)
