"""This is an implemntation of quick_sort."""


def quick_sort(numbers):
    import pdb; pdb.set_trace()
    pivot = numbers[0]
    pivot_index = numbers.index(pivot)
    store_index = numbers.index(pivot) + 1
    for i in numbers[1:]:
        if i < pivot:
            new_nums = [pivot]
            bigger_nums = []
            check_list = list(numbers[store_index:])
            count = 0
            for number in check_list:
                count += 1
                thing = check_list[count]
                print(number)
                print(thing)
                if number < pivot:
                    number, check_list[store_index] = check_list[store_index], number
                    store_index += 1
                print(new_nums)
                print(check_list)
            # pivot, check_list[store_index - 1] = check_list[store_index - 1], pivot
