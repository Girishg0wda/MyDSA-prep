activities = [
    (1, 3),
    (2, 4),
    (3, 5),
    (6, 8)
]

activities.sort(key=lambda x: x[1])

selected = [activities[0]]

last_finish = activities[0][1]

for start, finish in activities[1:]:
    if start >= last_finish:
        selected.append((start, finish))
        last_finish = finish

print(selected)