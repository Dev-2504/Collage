# Fibonacci Sequence using Dynamic Programming (Tabulation)

n = int(input("Enter the number of terms: "))

# List to store Fibonacci numbers
fib = [0] * n
fib[0] = 0
if n > 1:
    fib[1] = 1

# Fill the list using Dynamic Programming
for i in range(2, n):
    fib[i] = fib[i-1] + fib[i-2]

# Print the sequence
print("Fibonacci Sequence:")
for num in fib:
    print(num, end=" ")
