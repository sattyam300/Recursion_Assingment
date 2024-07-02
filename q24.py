def find_min(arr, n):
    if n == 1:
        return arr[0]
    else:
        return min(arr[n - 1], find_min(arr, n - 1))


my_array = [1, 4, 45, 6, -50, 10, 2]
min_value = find_min(my_array, len(my_array))
print(f"Minimum: {min_value}")

def find_max(arr, n):
    if n == 1:
        return arr[0]
    else:
        return max(arr[n - 1], find_max(arr, n - 1))

max_value = find_max(my_array, len(my_array))
print(f"Maximum: {max_value}")