# Mini Challenge 2
# Select maximum activities:
# activities = [
#     (1, 2),
#     (2, 3),
#     (3, 4),
#     (1, 5)
# ]
# Expected:
# [(1,2), (2,3), (3,4)]


activities = [
    (1, 2),
    (2, 3),
    (3, 4),
    (1, 5)
]

activities.sort(key=lambda x: x[1])

selected = [activities[0]]

last_finish = activities[0][1]

for start, finish in activities[1:]:
    if start >= last_finish:
        selected.append((start, finish))
        last_finish = finish

print(selected)