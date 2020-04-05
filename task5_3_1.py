couples = {}
with open('task5_3_2.txt', 'r') as sal:
    my_num = []
    min_num = []
    nums = sal.read().split()
    d = len(nums) / 2

    for i in range(0, len(nums)):
        if i % 2:
            my_num.append(nums[i])
            s = sum(map(float, my_num))
print('The average salary at Olympus:', s / d, min_num)
