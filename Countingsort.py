def counting_sort(array):
    # Find the maximum element in the array to know the range of the count array
    max_val = max(array)
    # Initialize count array with zeros, size determined by the max value in arr
    count_arr = [0] * (max_val + 1)

    # Store the count of each element in count_arr
    for item in array:
        count_arr[item] += 1

    # Modify count_arr by adding the previous counts (cumulative count)
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # Output array that will have sorted arr
    output_arr = [0] * len(array)

    # Build the output array using count_arr and input arr
    # Iterate backwards to maintain the stability of the sorting algorithm
    for item in reversed(array):
        output_arr[count_arr[item] - 1] = item
        count_arr[item] -= 1

    return output_arr


# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array is:", sorted_arr)