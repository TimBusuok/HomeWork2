# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.


# 10 -> 1 2 4 8

N = int(input("Введите число: "))
array = []


ans = False
for i in range(N):
    k = 2 ** i
    if k < N:
        array.append(k)
        ans = True
print(f"{N} -> {array}")
    
