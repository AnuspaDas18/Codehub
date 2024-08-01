def divisible_by_7_not_5():
    result = []
    for i in range(1000, 2001):
        if i % 7 == 0 and i % 5 != 0:
            result.append(i)
    return result

# Example usage
print(divisible_by_7_not_5())
