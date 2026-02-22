x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
d1 = ((x2-x1) + (y2-y1))**0.5
d2 = ((x3-x2) + (y3-y2))**0.5
d3 = ((x3-x1) + (y3-y1))**0.5
p = d1 + d2 + d3
print(p)