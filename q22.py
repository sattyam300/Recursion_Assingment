def sum_array(arr, size):
    if size == 0:
        return 0
    else:
        return arr[size - 1] + sum_array(arr, size - 1)

my_array = [1, 2, 3, 4, 5]
total_sum = sum_array(my_array, len(my_array))
print("Sum of array elements:", total_sum)