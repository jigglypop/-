# def quicksort(A, low, high):
#     def partition(low, high):
#         pivot = A[high]
#         left = low
#         for right in range(low, high):
#             if A[right] < pivot:
#                 A[left], A[right] = A[right], A[left]
#                 left += 1
#         A[left], A[high] = A[high], A[left]
#         return left
#     if low < high:
#         pivot = partition(low, high)
#         quicksort(A, low, pivot-1)
#         quicksort(A, pivot+1, high)


# print(quicksort([4, 1, 2, 3], 0, 3))
def QuickSort(input_list):
    if len(input_list) < 2:
        return input_list

    pivot = input_list[0]
    less = [i for i in input_list[1:] if i <= pivot]
    greater = [i for i in input_list[1:] if i > pivot]

    input_list = QuickSort(less) + [pivot] + QuickSort(greater)

    return input_list


print(QuickSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
