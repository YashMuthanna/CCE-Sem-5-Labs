# Caching - technique used to store and retrieve values that have been computed before, in order
# to avoid redundant computations and improve performance

def fibonacci(n, dic={}):
    if n in dic:
        return dic[n]
    if n <= 1:
        return n
    #If n is found in the cache, it means that the Fibonacci value for that n has already been
    # calculated and stored in the dictionary. So, the function can simply return the cached value using return cache[n].
    #If n is not found in the cache, the function proceeds to calculate the Fibonacci value for that
    # n using the recursive calculation logic
    result = fibonacci(n - 1, dic) + fibonacci(n - 2, cache)
    dic[n] = result
    return result

n = int(input("Enter a number: "))
fibonacci_result = fibonacci(n)
print("Fibonacci(", n, ") =", fibonacci_result)

