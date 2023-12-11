# Sorting Algorithm 1: Bubble Sort
#
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#write the list to be used
unsorted_list = [14, 27, 8,-42, 11, 35, -9, 56, 23]

bubble_sort_result = unsorted_list.copy()# to copy
bubble_sort(result_of_Bubble_Sorting)
print("The result of Bubble Sorting is", result_of_Bubble_Sorting)
# Output: Bubble Sort Result: [8, 9, 11, 14, 23, 27, 35, 42, 56]

# Complexity Classes (Bubble Sort): O(n^2)



# Sorting Algorithm 2: Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

#write the list to be used
unsorted_list = [14, 27, 8,-42, 11, 35, -9, 56, 23]

quick_sort_result = quick_sort(unsorted_list.copy())# to copy
print("The result of Quick Sorting is :", quick_sort_result)
# Output: Quick Sort Result: [8, 9, 11, 14, 23, 27, 35, 42, 56]

# Complexity Classes (Quick Sort): O(n log n)