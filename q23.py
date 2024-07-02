def find_mean(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return (find_mean(arr[:-1]) * (len(arr) - 1) + arr[-1]) / len(arr)

my_array = [1, 2, 3, 4, 5]
mean_value = find_mean(my_array)
print(f"Mean: {mean_value:.2f}")