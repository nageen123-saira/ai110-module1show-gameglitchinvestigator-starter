
def count_occurrences(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    return counts

nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))