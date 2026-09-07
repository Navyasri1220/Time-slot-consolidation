# Time-slot-consolidation
n = int(input())

intervals = []
for _ in range(n):
    start, end = map(int, input().split())
    intervals.append((start, end))


intervals.sort()

merged = []

for start, end in intervals:
    if not merged or start > merged[-1][1]:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

for start, end in merged:
    print(start, end)
