def get_prime(N: int):
    """ Sieve of Eratosthenes, function for getting prime number
    Args:
        N (int): this function return the array of prime number below this value
    """
    prime = []
    arr = [1]*(N+1)
    arr[0], arr[1] = 0, 0
    for i in range(2, N+1):
        if arr[i]:
            prime.append(i)
            for j in range(2 * i, N+1, i):
                arr[j] = 0

    return prime
