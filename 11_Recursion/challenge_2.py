# Challenge 2
# Return:
# 1 + 2 + 3 + 4
# using recursion.
# Expected:
# 10

def recursive_sum(n):
    if n == 1:
        return 1

    return n + recursive_sum(n - 1)

print(recursive_sum(4))