nums = [1, 2, 3]

result = []

def backtrack(path):
    if len(path) == len(nums):
        result.append(path[:])
        return

    for num in nums:
        if num in path:
            continue

        path.append(num)

        backtrack(path)

        path.pop()

backtrack([])

print(result)
print("Total permutations:", len(result))