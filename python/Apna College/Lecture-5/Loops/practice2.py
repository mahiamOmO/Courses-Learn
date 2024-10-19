nums = (1, 4, 9, 16, 24, 36, 49, 64, 81, 100)

x = 36

i = 0
while i < len(nums):
    if nums[i] == x:
        print("found at idx", i)
    i += 1
else:
    print("findin....")