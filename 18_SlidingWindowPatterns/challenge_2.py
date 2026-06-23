# Find length of longest substring without repeating characters.
# s = "pwwkew"
# Expected:
# 3
# Because:
# wke

s = "pwwkew"

left = 0
seen = set()
max_length = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])

    max_length = max(max_length, right - left + 1)

print(max_length)