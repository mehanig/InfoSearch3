#python3
import math

c = int(input())
a = [0 for _ in range(c)]
inp_arr = input().split(" ")
for i in range(c):
	a[i] = int(inp_arr[i])
PLook = 1 - 0.15
PFound = 0.0
for i in range(c):
	PFound += PLook * ( 2 ** (a[i] - 3) - 1 ) 
print(PFound)