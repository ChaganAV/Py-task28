def sum(a,b):
    if b>0:
        a = a + 1
        return sum(a,b-1)
    else:
        return a

try:
    a = int(input("Введите первое неотрицательное слагаемое: "))
    b = int(input("Введите второе неотрицательное слагаемое: "))
    if a>=0 and b>=0:
        res = sum(a,b)
        print(res)
    else:
        print("Sorry, введите положительные числа")
except:
    print("Что-то пошло не так")