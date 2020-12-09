"""https://adventofcode.com/2020/day/9"""

from itertools import combinations

numbers = [int(line.strip()) for line in open("inputs/09.txt", "r")]
preamble_size = 25


def traverse(nums):
    i = preamble_size
    while i < len(nums):
        if nums[i] not in [sum(el) for el in combinations(nums[i - preamble_size:i], 2)]:
            return nums[i]
        i += 1


def find_sum(nums, val, size=2):
    i = 0
    temp_size = size
    while i < len(nums) and size < len(nums):
        try:
            nums_list = nums[i:i+temp_size]
            curr = sum(nums_list)
            if curr == val:
                max_no = max(nums_list)
                min_no = min(nums_list)
                return max_no + min_no
            if curr < val:
                temp_size += 1
            if curr > val:
                temp_size = 2
                i += 1
        except IndexError:
            print('Out of range')


invalid_number = traverse(numbers)
print(invalid_number)
print(find_sum(numbers, invalid_number))
