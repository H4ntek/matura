import math

clock = [[], [], []]
temp = [[], [], []]
BASE = [2, 4, 8]
N = 1095
INF = 10**100

for i in range(3):
    in1 = open(f"dane_systemy{i + 1}.txt", "r+")
    for line in in1:
        c, t = line.strip().split()
        minus = 1
        if str(t)[0] == "-":
            t = t[1:]
            minus = -1
        clock[i].append(int(c, BASE[i]))
        temp[i].append(minus * int(t, BASE[i]))
    in1.close()

# 58.1.
mn = [INF, INF, INF]
for i in range(N):
    for j in range(3):
        mn[j] = min(mn[j], temp[j][i])
print(f"58.1.\nMinimalne temperatury: {['', '-'][mn[0] < 0] + bin(abs(mn[0]))[2:]} dla S1, {['', '-'][mn[1] < 0] + bin(abs(mn[1]))[2:]} dla S2, {['', '-'][mn[2] < 0] + bin(abs(mn[2]))[2:]} dla S3.\n\n")

# 58.2.
ans = 0
for i in range(N):
    all_broken = True
    for j in range(3):
        all_broken &= (clock[j][i] != 12 + i * 24)
    ans += all_broken
print(f"58.2.\n{ans} razy odczyt zegara był nieprawidłowy jednocześnie we wszystkich stacjach.\n\n")

# 58.3.
ans = 0
mx = [-INF, -INF, -INF]
for i in range(N):
    record = False
    for j in range(3):
        record |= (i == 0 or temp[j][i] > mx[j])
        mx[j] = max(mx[j], temp[j][i])
    ans += record
print(f"58.3.\nByło {ans} dni rekordowych.\n\n")

# 58.4.
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        ans = max(ans, math.ceil((temp[0][i] - temp[0][j])**2 / abs(i - j)))
print(f"58.4.\nMax. skok temperatury w stacji S1: {ans}.")
