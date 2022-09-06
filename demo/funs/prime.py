def prime(number: int) -> bool:
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False

    return True


print(prime(7))
