t = int(input())
nums = [input() for _ in range(t)]

for i in range(t):
    a = int(nums[i].replace('4', '2'))
    b = int(nums[i]) - a
    print('Case #' + str(i + 1) + ': ' + str(a) + ' ' + str(b))
