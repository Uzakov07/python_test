n, m = [int(i) for i in input("Введите размер n и m:").split()]
a = [[int(j) for j in input("Введите значения :").split()] for i in range(n)]
for i in range(n):
    for j in range(m-1):
        if a[i][j] < a[i][j+1]:
            temp=a[i][j]
            a[i][j]=a[i][j+1]
            a[i][j+1]=temp
print("После сортировки")
for i in range(n):
    for j in range(m):
        print(a[i][j])
    print("\n")
print("После возведение в квадрат")
for i in range(n):
    for j in range(m):
        if a[i][j] % 3 == 0:
            a[i][j] = a[i][j]**2
for i in range(n):
    for j in range(m):
        print(a[i][j])
    print("\n")