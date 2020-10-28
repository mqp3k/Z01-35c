import sys

nums = []

for n in range(1, len(sys.argv)):
    nums.append(int(sys.argv[n]))

nums.sort()
print(nums)