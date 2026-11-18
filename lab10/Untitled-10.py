def stats(nums):
    stat = (min(nums), max(nums), sum(nums)/len(nums))
    return stat

nums = list(map(int, input().split()))

print(stats(nums))
