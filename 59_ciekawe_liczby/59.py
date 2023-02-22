in1 = open("liczby.txt", "r+")
a = []
for line in in1:
    a.append(int(line.strip()))

# 59.1.
def factorize(x):
    i = 3
    f = []
    n = x
    while i * i <= x:
        if n % i == 0:
            f.append([i, 1])
            while n % i == 0:
                n //= i
                f[-1][1] += 1
        i += 2
    if n > 1:
        f.append([n, 1])
    return f

cnt = 0
for x in a:
    if x % 2 == 0:
        continue
    f = factorize(x)
    cnt += (len(f) == 3)
print(f"59.1.\nJest {cnt} takich liczb.") 

# 59.2.
cnt = 0
for x in a:
    cnt += str(int(x) + int(str(x)[::-1])) == str(int(x) + int(str(x)[::-1]))[::-1]
print(f"\n59.2.\nJest {cnt} takich liczb.")

# 59.3.
def digit_product(x):
    ans = 1
    while x:
        ans *= (x % 10)
        x //= 10
    return ans

cnt = [0 for i in range(0, 9)]
mn = 10**100
mx = 0
for x in a:
    k = 0
    n = x
    while n >= 10:
        n = digit_product(n)
        k += 1
    if k <= 8:
        cnt[k] += 1
    if k == 1:
        mn = min(mn, x)
        mx = max(mx, x)
print("\n\n59.3.")
for i in range(1, 9):
    print(f"Jest {cnt[i]} liczb o mocy {i}.")
print(f"Max. liczba o mocy 1: {mx}")
print(f"Min. liczba o mocy 1: {mn}")
