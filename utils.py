def find_max(numbers):
    max_no = numbers[0]
    for i in numbers:
        if i > max_no:
            max_no = i

    return max_no
