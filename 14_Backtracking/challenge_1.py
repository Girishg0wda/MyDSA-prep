# Generate all subsets of:
# nums = [1, 2, 3]
# Just run the subset code with this input.
# Expected number of subsets:
# 8
# Because:
# 2^3 = 8

nums = [1, 2, 3]

result = []

def backtrack(start, path):
    result.append(path[:])

    for i in range(start, len(nums)):
        path.append(nums[i])

        backtrack(i + 1, path)

        path.pop()

backtrack(0, [])

print(result)
print("Total subsets:", len(result))