def fibonacci(n):
    if n <= 0:
        return "Invalid output"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(1, 25):
        print(fibonacci(i),end=" ")