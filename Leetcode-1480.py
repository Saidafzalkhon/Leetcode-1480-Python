nums = list(map(int,input().split()))
num1 = list()
son = 0
for i in range(len(nums)):
    for j in range(i+1):
        son += nums[j]
    num1.append(son)
    son = 0
print(num1)