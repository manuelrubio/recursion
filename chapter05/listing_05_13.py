def partition_Hoare_rec(a, left, right, pivot):
    if left > right:
        return right
    else:
        if a[left] > pivot and a[right] <= pivot:
            aux = a[left]
            a[left] = a[right]
            a[right] = aux
            return partition_Hoare_rec(a, left + 1,
                                       right - 1, pivot)
        else:
            if a[left] <= pivot:
                left = left + 1
            if a[right] > pivot:
                right = right - 1
            return partition_Hoare_rec(a, left, right, pivot)


def partition_Hoare_wrapper(a, lower, upper):
    if upper >= 0:
        middle = (lower + upper) // 2
        pivot = a[middle]
        a[middle] = a[lower]
        a[lower] = pivot

        right = partition_Hoare_rec(a, lower + 1, upper, pivot)

        a[lower] = a[right]
        a[right] = pivot

        return right


# Test
a = [4, 6, 0, 3, 5, 7, 4, 5, 2, 1]
b = a.copy()
print(a)
pivot_index = partition_Hoare_wrapper(a, 0, len(a) - 1)
print('Pivot index = ', pivot_index,
      ', Pivot = ', b[pivot_index], sep='')
print(a)
