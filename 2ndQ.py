#SecondQuestion

def fibonacci(limit):
    fib_series = []
    a, b, summary = 1, 2, 0
    while a <= limit:
        fib_series.append(a)
        if a%2==0:
            summary +=a
        a, b = b, a + b
    return fib_series,summary

# Fibonacci serisinin 50'ye kadar olan elemanlarını hesaplayalım
limit = 4000000
fibonacciseries, summary = fibonacci(limit)
print(fibonacciseries)
print(summary)


