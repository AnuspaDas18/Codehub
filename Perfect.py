def is_perfect_number(n):
    sum_of_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_of_divisors == n

# Example usage
print(is_perfect_number(28))
