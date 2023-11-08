file = open("alfie.txt", "r")
for i in range(21):
    print(file.read(4))
file.close()

primes = {1: 2, 2: 3, 4: 7, 7:17}
print(primes[primes[4]])

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))

nums = [i*2 for i in range(10)]
print(nums)

nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))

triple = lambda x: x * 3
add = lambda x, y: x + y
print(add(triple(3), 4))