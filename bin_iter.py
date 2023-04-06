def binsearch(numbers, target):
    left = 0
    right = len(numbers)-1

    while left <= right:
        mid = (left+right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main():
    numbers = [10, 20, 25, 30, 50, 70, 80]
    target = 70

    ret = binsearch(numbers, target)
    if ret != -1:
        print(f'Found {target} at the index {ret}')
    else:
        print('Not Found')


if __name__ == '__main__':
    main()
