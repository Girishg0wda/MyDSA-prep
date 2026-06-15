# Challenge 1
# Create:
# countdown(5)
# Output:
# 5
# 4
# 3
# 2
# 1

def countdown(n):
    if n == 0:
        return

    print(n)

    countdown(n - 1)

countdown(5)