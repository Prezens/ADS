import time

end_time = 0
count_iteration = 0


def merge_sort(array):
    global count_iteration
    count_iteration += 1

    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    return merge(left, right)


def merge(left, right):
    global count_iteration
    count_iteration += 1

    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right

    return result


def run(array, filter):
    global end_time
    start_time = time.perf_counter()

    sorted_array = merge_sort(array)

    end_time = (time.perf_counter() - start_time)

    if filter == 1:
        return sorted_array[::-1]
    elif filter == 0:
        return sorted_array
