word = "aabbcde"

counts = {}

for ch in word:
    counts[ch] = counts.get(ch, 0) + 1

print(counts)