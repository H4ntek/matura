in1 = open("ciagi.txt", "r+")

a = []
for _ in range(0, 100):
    n = int(in1.readline())
    s = in1.readline()
    s = list(map(int, s.split()))
    a.append(s)

# 61.1.
def check(s):
    d = set()
    for i in range(1, len(s)):
        d.add(s[i] - s[i - 1])
    return list(d)[0] if len(d) == 1 else False

ok = ans = mx = 0
best = []
for s in a:
    ok = check(s)
    if ok:
        ans += 1
        if ok > mx:
            mx = ok
            best = s
print(f"61.1\nJest {ans} ciągów arytmetycznych, największa różnica to {mx}, posiada ją ciąg:")
for x in best:
    print(x, end = " ")

# 61.2.
print("\n\n61.2")
cubes = [i**3 for i in range(1, 101)]
for s in a:
    here = 0
    for x in s:
        if x in cubes:
            here = x
    if here != 0:
        print(here, end = " ")

# 61.3.
in1 = open("bledne.txt", "r+")
a = []
for _ in range(0, 20):
    n = int(in1.readline())
    s = in1.readline()
    s = list(map(int, s.split()))
    a.append(s)

print("\n\n61.3.")
for s in a:
    mp = {}
    for i in range(1, len(s)):
        if s[i] - s[i - 1] not in mp.keys():
            mp[s[i] - s[i - 1]] = 1
        else:
            mp[s[i] - s[i - 1]] += 1
    d = mx = 0
    for k, v in mp.items():
        if v > mx:
            mx = v
            d = k
    for i in range(1, len(s)):
        if s[i] - s[i - 1] != d:
            print(s[i], end = " ")
            break
