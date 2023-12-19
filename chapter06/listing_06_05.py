def quick_sort_inplace(a, lower, upper):
    if lower < upper:
        pivot_index = partition_Hoare_wrapper(a, lower, upper)

        quick_sort_inplace(a, lower, pivot_index - 1)
        quick_sort_inplace(a, pivot_index + 1, upper)


# Test
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


a = []
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()

a = [5]
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()

a = [3, 5]
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()

a = [5, 3]
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()

a = [1, 3, 5]
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()

a = [1, 5, 3]
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()

a = [3, 1, 5]
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()

a = [3, 5, 1]
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()

a = [5, 1, 3]
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()

a = [5, 3, 1]
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()

a = [72, 28, 30, 80, 18, 94, 54, 95, 12, 6, 26, 43, 18]
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()
