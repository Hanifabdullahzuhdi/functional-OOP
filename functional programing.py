def count_elements(lst):
    return reduce(lambda x, _: x + 1, lst, 0)
