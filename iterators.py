# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

fig = int(input())
string = input().split()
k = int(input())
count = 0
total = 0
comby = list(combinations(string, k))

for i in comby:
    if "a" in i:
        count +=1
    total += 1

print(count/total)
