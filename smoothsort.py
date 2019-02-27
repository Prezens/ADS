import heapq
import time

end_time = 0


def numbers_leonardo(size):
    numbers = [1, 1]
    next_number = numbers[-1] + numbers[-2] + 1
    while len(numbers) >= 2 and size > next_number:
        numbers.append(next_number)
        next_number = numbers[-1] + numbers[-2] + 1
    numbers.reverse()
    return numbers


def do_list_heaps(data):
    leonardo_numbers = numbers_leonardo(len(data))
    list_heaps = []
    m = 0
    for i in leonardo_numbers:
        if len(data) - m >= i:
            list_heaps.append(data[m: m + i])
            m += i
    for i in list_heaps:
        heapq.heapify(i)

    list_heaps.reverse()
    return list_heaps


def count_indexes(i, indexes):
    indexes.append(2 * indexes[i] + 1)
    indexes.append(2 * indexes[i] + 2)

    return indexes


def get_list(indexPart, heap):
    heap_part = []
    for i in indexPart:
        if i < len(heap):
            heap_part.append(heap[i])

    return heap_part


def heap_division(heap):
    index = 0
    indexes_left = [1]
    indexes_right = [2]
    while indexes_left[-1] < len(heap):
        indexes_left = count_indexes(index, indexes_left)
        indexes_right = count_indexes(index, indexes_right)

        index += 1

    heap_left = get_list(indexes_left, heap)
    heap_right = get_list(indexes_right, heap)

    return heap_left, heap_right


def smooth_sort(list_heaps):
    heap_left = None
    heap_right = None
    result = []

    while list_heaps:
        flag = 0
        min_index = list_heaps.index(min(list_heaps))
        current_root = list_heaps[0][0]
        current_min = list_heaps[min_index][0]
        heapq.heapreplace(list_heaps[0], current_min)
        heapq.heapreplace(list_heaps[min_index], current_root)

        if len(list_heaps[0]) > 1:
            heap_left, heap_right = heap_division(list_heaps[0])
            flag = 1

        minimum = heapq.heappop(list_heaps[0])
        result.append(minimum)
        list_heaps.pop(0)

        if flag == 1:
            list_heaps.insert(0, heap_left)
            list_heaps.insert(0, heap_right)

    return result


def run(input_list):
    global end_time
    start_time = time.perf_counter()

    input_list_heaps = do_list_heaps(input_list)
    sorted_input_list = smooth_sort(input_list_heaps)

    end_time = (time.perf_counter() - start_time)

    return sorted_input_list
