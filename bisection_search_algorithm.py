def search(l: list, q: int):
    ''' (list, int) -> int '''
    low = 0
    high = len(l) - 1
    mid = (low + high) // 2
    guess = l[mid]

    if q == 0:  # только для возрастающей положительной последовательности целых чисел
        if l[0] == 0:
            return 0
        else:
            raise ValueError
    else:
        while low < high:

            if q > guess:
                low = mid + 1
            else:
                high = mid
            mid = (low + high) // 2
            guess = l[mid]

        if guess == q:
            return mid

        else:
            raise ValueError

a = [0, 1, 6, 7, 7, 9, 9, 9, 9, 9, 8, 12, 34, 45, 99, 1000]
print(search(a, 7))
print(search(a, 9))
print(search(a, 45))
# print(search(a, v))
# print(search(a, 3))


