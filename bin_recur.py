
def binsearch_recur(numbers, left, right, target):

    if left <= right:
        mid = (left+right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
            return binsearch_recur(numbers, left, right, target)
        else:
            right = mid - 1
            return binsearch_recur(numbers, left, right, target)
    else:
        return -1


def main():
    # import random
    # numbers = [random.randint(0, 100) for i in range(10)]
    # numbers.sort()
    numbers = [10, 20, 25, 30, 50, 70, 80]
    target = 70

    print(f'Initial list values: {numbers}')

    ret = binsearch_recur(numbers, 0, len(numbers)-1, target)
    if ret != -1:
        print(f'Found at {ret}, {numbers[ret]}')
    else:
        print(f'Not Found, {target}')


if __name__ == '__main__':
    main()


print ()