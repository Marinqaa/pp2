# 1
def gramtoounce(a):
    ounces = 28.3495231 * a
    return ounces

a = int(input())
print(gramtoounce(a))

# 2
def temperature(f):
    c = (5 / 9) * (f-32)
    return c
far = int(input())
print(temperature(far))

# 3
def solve(numlegs, numheads):
    for i in range(1, numheads+1):
        if (i*4)+(numheads-i)*2 == numlegs:
            ans = f"{i} rabbits,{numheads-i} chickens"
            return ans
print("Enter number of legs:")
numlegs=int(input())
print("Enter number of heads")
numheads=int(input())
print(solve(numlegs, numheads))
# 4
def filter_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("Enter size of list:")
n = int(input())
print("Enter elements of list:")
l = list()
for i in range(n):
    x = int(input())
    if filter_prime(x):
        l.append(x)
print(l)

# 5
def factorial(a):
    fact = 1
    for i in range(1, a + 1):
        fact = fact * i
    return fact

permut = str(input())
print(factorial(len(permut)))

# 6
def reverse(w):
    rev = w.split()
    return ' '.join(reversed(rev))

w = str(input())
print(reverse(w))






