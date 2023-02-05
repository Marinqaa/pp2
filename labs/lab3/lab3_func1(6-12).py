# 7
def has_33(nums):
    return any(nums[i + 1] == nums[i] == 3 for i in range(len(nums) - 1))

nums = list(map(int, input().split()))
print(has_33(nums))

# 8
def spy_game(nums1):
    a = ''.join(nums1)
    for i in nums1:
        if '007' in a:
            return True
    return False

nums1 = list(map(str, input().split()))
print(spy_game(nums1))

# 9
import math
def volume(r): #V = 4pir^3/3
    vol = (4*math.pi * r**3)/3
    return vol

r = float(input())
print(volume(r))

# 10
def unique_list(l):
  empty = []
  for a in l:
    if a not in empty:
      empty.append(a)
  return empty
list1 = list(map(int, input().split()))
print(unique_list(list1))
# 11
def palindrome(w):
    if w == w[::-1]:
        return "Yes, it is palindrome"
    else:
        return "Not palindrome"
w = str(input())
print(palindrome(w))


# 12
def histogram(list):
    for i in range(0, len(list)):
        print('*' * list[i])
    return
list2 = list(map(int, input().split()))
print(histogram(list2))
