Problem-1
Time slot consolidation.py
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
input 
4
1 3
2 6 
8 10
15 18
output
1 6
8 10
15 18
Problem-2
Maximum signal strength.py
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, n):
    window_sum += arr[i] - arr[i - k]
    max_sum = max(max_sum, window_sum)

print(max_sum)
Input
6
2 1 5 1 3 2
3
Output
9
Problem-3
Communication Channel Analyzer Problem Statement.py
s = input().strip()

last_seen = [-1] * 26
left = 0
max_len = 0

for right, ch in enumerate(s):
    idx = ord(ch) - ord('a')

    if last_seen[idx] >= left:
        left = last_seen[idx] + 1

    last_seen[idx] = right
    max_len = max(max_len, right - left + 1)

print(max_len)

