def first_last6(nums):
  if nums[0] == 6 or nums[len(nums)-1] == 6:
    return True
  return False

def same_first_last(nums):
  if len(nums) >= 1:
    if nums[0] == nums[len(nums) - 1]:
      return True
  return False

def make_pi():
  return [3, 1, 4]

def common_end(a, b):
  if a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1]:
    return True
  return False

def sum3(nums):
  counter = 0
  for n in nums:
    counter += n
  return counter

def rotate_left3(nums):
  x = nums[0]
  nums[0] = nums[2]
  nums[2] = x
  x = nums[0]
  nums[0] = nums[1]
  nums[1] = x
  return nums

def reverse3(nums):
  return nums[::-1]

def max_end3(nums):
  if nums[0] > nums[2]:
    nums = [nums[0],nums[0],nums[0]]
  else:
    nums = [nums[2], nums[2], nums[2]]
  return nums

def sum2(nums):
  if len(nums) == 0:
    return 0
  elif len(nums) < 2:
    return nums[0]
  else:
    return nums[0] + nums[1]

def middle_way(a, b):
  return [a[1], b[1]]

def make_ends(nums):
  return [nums[0], nums[-1]]

def has23(nums):
  if nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3:
    return True
  return False

arr = [0,1,2,3,6]
a = [1, 2, 3]
b = [7, 3]

print(first_last6(arr))
#should be true

print(same_first_last(arr))
#should be false 

print(make_pi())
#should be [3, 1, 4]

print(common_end(a,b))