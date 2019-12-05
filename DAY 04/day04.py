from collections import defaultdict

def performCheck(num):
    repeatCnt = defaultdict(int)
    decreases = False

    for i in range(len(num)):
        if i > 0 and num[i] == num[i - 1]:
            repeatCnt[num[i]] += 1
        if i > 0 and num[i] < num[i - 1]:
            decreases = True
    return repeatCnt, decreases 

nums = map(str, range(193651, 649729))

#part 1
solutions1 = 0
for num in nums:
    repeatCnt, decreases = performCheck(num)
    if len(repeatCnt) > 0 and not decreases:
        solutions1 += 1    
print(solutions1)

#part 2
solutions2 = 0
for num in nums:
    repeatCnt, decreases = performCheck(num)
    has_adjacent = 1 in repeatCnt.values()
    if has_adjacent and not decreases:
        solutions2 += 1
print(solutions2)


