
def caching_fibonacci():
    """
    Caching Fibonacci.
    :return: function calculator.
    """
    cache = {} # A dictionary to save previously computed values.

    def fibonacci(n):
        # If n out of scope we just return
        if n <= 0:
            return 0
        # Fibonacci(1) will always be 1, just return 1.
        if n == 1:
            return 1

        # Return value from cache if it exists.
        # We don't calculate it again.
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]
    # END: def fibonacci(n):

    return fibonacci
# END: def caching_fibonacci():

# Receive fibonacci function.
fibo = caching_fibonacci()

print(fibo(10))  # Print 55
print(fibo(15))  # Print 610