def quickselect(a, lower, upper, k):
    if lower == upper:
        return a[lower]
    else:
        pivot_index = partition_Hoare_wrapper(a, lower, upper)

        if pivot_index == k - 1:
            return a[pivot_index]
        elif pivot_index < k - 1:
            return quickselect(a, pivot_index + 1, upper, k)
        else:
            return quickselect(a, lower, pivot_index - 1, k)


# Test
def partition_Hoare_rec(a, left, right, pivot):
    if left > right:
        return right
    else:
        if a[left] > pivot and a[right] <= pivot:
            aux = a[left]
            a[left] = a[right]
            a[right] = aux
            return partition_Hoare_rec(a, left + 1, right - 1, pivot)
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


a = [4, 2, 5, 4, 8, 7, 1, 4, 3, 2, 6, 5, 4]
for i in range(0, len(a)):
    v = list(a)
    print(quickselect(v, 0, len(v) - 1, i + 1))
