def mergeSort(arr):
    if len(arr) == 1:
        return arr

    middle = len(arr) // 2

    left_half = mergeSort(arr[:middle])
    right_half = mergeSort(arr[middle:])

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1;
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


if __name__ == "__main__":
    arr = [1, 8, 5, 0, 3, 4, 2, 9, 7, 6]
    print(mergeSort(arr))
