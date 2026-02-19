# 10 001st Prime
def get_nth_prime(n):
    primes = [2]
    num = 3
    while len(primes) < n:
        is_prime = True
        limit = num**0.5
        for p in primes:
            if p > limit:
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 2
    return primes[-1]

print(get_nth_prime(10001))
