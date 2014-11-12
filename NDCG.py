#python3
import math

c = int(input())
a = [0 for _ in range(c)]
inp_arr = input().split(" ")
for i in range(c):
	a[i] = int(inp_arr[i])
DCG = 0.0
Z = 0.0
for i in range(c):
	DCG += ( 2 ** a[i] - 1) / (math.log((i+2),2)) 
	Z += ( 2 ** 3 - 1) / (math.log((i+2),2))
print(DCG/Z)