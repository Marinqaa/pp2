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
def solve(num_heads, num_legs):
    ns = "No solutions!"
    for i in range(num_heads + 1):
        j = num_heads - i
        if 2 * i + 4 * j == num_legs:
            return i, j
    return ns, ns


if __name__ == "__main__":
    numheads = 35
    numlegs = 94

    solutions = solve(numheads, numlegs)
    print(solutions)

# 4
def isPrime(nums):
    for i in nums:
        if nums[i] == 1 or nums[i] == 2 or nums[i] == 3:
            return True
        elif nums[i] % 2 == 0:
            return False
        for n in range(2, len(nums)):
            if nums[i] % n == 0:
                return False
        return True


nums = list(map(int, input().split()))
if isPrime(nums) == True:
    print(nums)

# 5
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
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





