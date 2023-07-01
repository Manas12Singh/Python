def rev(n: int, k: int = 0) -> int:
    if (n < 0):
        return ValueError("Only positive integers")
    if (n == 0):
        return k
    k = k*10+n % 10
    n //= 10
    return rev(n, k)