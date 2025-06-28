from collections import Counter

def mean(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    nums = sorted(numbers)
    n = len(nums)
    mid = n // 2
    return nums[mid] if n % 2 else (nums[mid - 1] + nums[mid]) / 2

def mode(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    count = Counter(numbers)
    max_count = max(count.values())
    return [num for num, freq in count.items() if freq == max_count]

