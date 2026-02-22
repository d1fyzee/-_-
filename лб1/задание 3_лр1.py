P = int(input())
X = int(input())
Y = int(input())
total_kopecks = X * 100 + Y
new_total_kopecks = total_kopecks + (total_kopecks * P // 100)
print(new_total_kopecks // 100, new_total_kopecks % 100)