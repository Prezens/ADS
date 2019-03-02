import random
import time
import mansurov_labs.smoothsort as smoothsort
import mansurov_labs.timsort as timsort


class LabOne:
    def __init__(self):
        self.__array = []
        self.__choice_sort = 0
        self.__choice_sort_filter = 0
        self.sorted_array = []
        self.__search_number = 0
        self.__len_array = 0
        self.iter_count_line = 0
        self.iter_count_binary = 0
        self.timer_binary = 0
        self.timer_line = 0

    def setter(self, array_values, number, len_array, choice_s, choice_s_f):
        self.__array = array_values
        self.__choice_sort = choice_s
        self.__choice_sort_filter = choice_s_f
        self.sorted_array = self.sort(array_values)
        self.__search_number = number
        self.__len_array = len_array

    def sort(self, array):
        if self.__choice_sort == 1:
            self.sorted_array = smoothsort.run(array)
        else:
            self.sorted_array = timsort.run(array)

        return self.sorted_array

    def line_search(self):
        start_time = time.perf_counter()

        for i in range(self.__len_array):
            self.iter_count_line += 1
            if self.__search_number == self.__array[i]:
                self.timer_line = (time.perf_counter() - start_time)
                return i

        self.timer_line = (time.perf_counter() - start_time)

        return None

    def binary_search(self):
        start_time = time.perf_counter()

        start = 0
        stop = len(self.sorted_array) - 1
        x = None

        if self.__choice_sort_filter:
            while start <= stop:
                self.iter_count_binary += 1

                middle = (start + stop) // 2

                if self.sorted_array[middle] == self.__search_number:
                    x = middle
                    self.timer_binary = (time.perf_counter() - start_time)
                    return x
                else:
                    if self.__search_number > self.sorted_array[middle]:
                        stop = middle - 1
                    else:
                        start = middle + 1
        else:
            while start <= stop:
                self.iter_count_binary += 1

                middle = (start + stop) // 2

                if self.sorted_array[middle] == self.__search_number:
                    x = middle
                    self.timer_binary = (time.perf_counter() - start_time)
                    return x
                else:
                    if self.__search_number < self.sorted_array[middle]:
                        stop = middle - 1
                    else:
                        start = middle + 1

        self.timer_binary = (time.perf_counter() - start_time)

        return x

    def iter_counter_line(self):
        return self.iter_count_line

    def iter_counter_binary(self):
        return self.iter_count_binary

    def print_result_line_search(self):
        result = self.line_search()

        if result is not None:
            print('Индекс искомого элемента в линейном поиске:', result)
        else:
            print('Искомый элемент не найден')

    def print_result_binary_search(self):
        result = self.binary_search()

        if result is not None:
            print('Индекс искомого элемента в бинарном поиске:', result)
        else:
            print('Искомый элемент не найден')

    def print_arrays(self, need_to_print_arrays):
        if need_to_print_arrays:
            print('\nВаш линейный массив имеет вид: ')
            for x in self.__array:
                print(x, end=' ')

            print('\n\nВаш бинарный массив имеет вид: ')
            for x in self.sorted_array:
                print(x, end=' ')
            print('\n')


def main():
    try:
        length_array = int(input('Длина массива > '))
        while length_array < 0:
            print('Вы ввели некорректные данные, повторите ввод')
            length_array = int(input('Длина массива > '))

        fill_array = int(input('Хотите заполнить массив самостоятельно[0] или случайными числами[1]? > '))
        while fill_array not in [0, 1]:
            print('Вы ввели некорректные данные, повторите ввод')
            fill_array = int(input('Хотите заполнить массив самостоятельно[0] или случайными числами[1]? > '))

        search_number = int(input('Искомое число > '))

        need_to_print_array = int(input('Если Вы хотите, чтобы массивы были напечатаны, то введите 1, иначе 0 > '))
        while need_to_print_array not in [0, 1]:
            print('Вы ввели некорректные данные, повторите ввод')
            need_to_print_array = int(input('Если Вы хотите, чтобы массивы были напечатаны, то введите 1, иначе 0 > '))

        choice_sort = int(input('Выберите алгоритм сортировки: Timsort[0], Smoothsort[1] > '))
        while choice_sort not in [0, 1]:
            print('Вы ввели некорректные данные, повторите ввод')
            choice_sort = int(input('Выберите алгоритм сортировки: Timsort[0], Smoothsort[1] > '))

        choice_sort_filter = int(input('Какую сортировку вы хотите применить для бинарного поиска 0[по возрастанию], 1[по убыванию] > '))
        while choice_sort_filter not in [0, 1]:
            print('Вы ввели некорректные данные, повторите ввод')
            choice_sort_filter = int(input('Какую сортировку вы хотите применить для бинарного поиска 0[по возрастанию], 1[по убыванию] > '))
    except ValueError:
        print('Вы ввели некорректный тип данных, повторите ввод\n')
        return main()

    array = []
    if fill_array == 0:
        array = list(map(int, input().split()))
    elif fill_array == 1:
        for i in range(length_array):
            array.append(random.randint(0, length_array * 3))

    lab = LabOne()
    lab.setter(array, search_number, length_array, choice_sort, choice_sort_filter)

    if need_to_print_array:
        lab.print_arrays(need_to_print_array)

    lab.print_result_line_search()
    lab.print_result_binary_search()

    print('\nКоличество итераций в Линейном поиске:', lab.iter_counter_line())
    print('Количество итераций в Бинарном поиске:', lab.iter_counter_binary())

    print('\nВремя выполнения Линейного поиска: {:.20f} секунд'.format(lab.timer_line))
    print('Время выполнения Бинарного поиска: {:.20f} секунд'.format(lab.timer_binary))

    if choice_sort == 1:
        print('Время выполнения Плавной сортировки: {:.20f} секунд'.format(smoothsort.end_time))
        print('Количество итераций Плавной сортировки:', smoothsort.count_iteration)
    else:
        print('Время выполнения сортировки Timsort: {:.20f} секунд'.format(timsort.end_time))
        print('Количество итераций сортировки Timsort:', timsort.count_iteration)


if __name__ == '__main__':
    main()
