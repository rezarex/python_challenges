arr = [1,2,3,4,5] 

maxVals = []
minVals = []
maxSum = 0
minSum = 0
for i in arr:
    maxVals.append(i)
maxVals.remove(min(maxVals))
#print(maxVals)

for i in arr:
    minVals.append(i)
minVals.remove(max(minVals))        
#print(minVals)

maxSum = sum(maxVals)
#print(maxSum)

minSum = sum(minVals)
#print(minSum)

print(minSum, maxSum)