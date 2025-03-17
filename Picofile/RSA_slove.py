from Crypto.Util.number import long_to_bytes

N = 16100414917200490684818090834030568375197524037435886882936555309624102396204036116564108271658868039859522044150809214611829088691020560068402537185199366
e = 65537
c = 2594427195049007279978555952644787815111139220943285891238788141919811150635476866016183209810264930663101151015039617413290206321283908833151234418057531
# Tách N thành 2 * q
q = N // 2

# Hàm kiểm tra nguyên tố Miller-Rabin
def is_prime(n, k=5):
    from random import randint
    if n < 2: return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = randint(2, min(n-2, 1<<20))
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(s-1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

if is_prime(q):
    # Tính φ(N) và khóa giải mã d
    phi = q - 1
    d = pow(e, -1, phi)
    # Giải mã
    m = pow(c, d, N)
    # Chuyển đổi sang bytes và in flag
    flag = long_to_bytes(m).decode()
    print(flag)
else:
    print("q không phải là số nguyên tố. Cần phân tích thêm q.")
