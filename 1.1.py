min = float('inf')
max = float('-inf')
sr = 0 
srqv = 0 
a = 0
k = 0 
arr = []
while a != 'end':
    a = input()
    if a == 'end':
        break
    arr.append(a)
    if int(a) > max :
        max = int(a)
    if int(a) < min :
        min = int(a)
    sr += int(a)
    k += 1

sr = sr / k
sum = 0

for i in arr: 
    sum += (float(i) - float(sr))**2
srqv = (sum / (k-1))**(1/2)

print(max, min, round(sr, 2), round(srqv,2))