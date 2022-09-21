#coding by Asa Whitman
import math
N = int(input("enter a number: "))
x = 1
z = 0
for i in range(N):
    y = x ** 3
    z += y
    x += 1
print(z)