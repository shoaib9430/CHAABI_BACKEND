def factorial(n):
    return (lambda f: lambda x: f(f, x))(lambda f, x: 1 if x == 0 else x * f(f, x - 1))(n)

# Example usage
number = 5
result = factorial(number)
print(result)
