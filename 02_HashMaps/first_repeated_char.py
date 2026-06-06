word = "abccba"

seen = set()

for letter in word:
    if letter in seen:
        print(letter)
        break

    seen.add(letter)