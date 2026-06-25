# Check if:
# s = "racecar"
# is a palindrome.
# Expected:
# True

s = "racecar"

left = 0
right = len(s) - 1

is_palindrome = True

while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

print(is_palindrome)