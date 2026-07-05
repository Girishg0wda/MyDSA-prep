word = "python"

stack = []

for ch in word:
    stack.append(ch)

reversed_word = ""

while stack:
    reversed_word += stack.pop()

print(reversed_word)