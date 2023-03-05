in1 = open("liczby.txt", "r+")
a = [int(x) for x in in1]

# 60.1.
cnt = 0
l = []
for x in a:
    if x < 1000:
        cnt += 1
        l.append(x)
print(f"60.1.\nJest {cnt} liczb mniejszych od 1000, ostatnie dwie: {l[-2]} i {l[-1]}.")

# 60.2.
def get_divs(x):
    i = 1
    d = []
    while i * i <= x:
        if x % i == 0:
            if i * i != x:
                d.append(i)
            d.append(x // i)
        i += 1
    d = sorted(d)
    d = [str(x) for x in d] # zmieniamy na stringi, bo .join działa tylko z listą stringów
    return d

print("\n60.2.")
for x in a:
    d = get_divs(x)
    if len(d) == 18:
        print(f"{x}: dzielniki: {', '.join(d)}")

# 60.3.
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

mx = 0
for i in range(200):
    ok = True
    for j in range(i + 1, 200):
        ok &= (gcd(a[i], a[j]) == 1)
    if ok:
        mx = max(mx, a[i])
print(f"\n60.3.\nLiczba {mx}.")
