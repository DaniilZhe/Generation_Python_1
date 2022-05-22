
# Chapter 2. Data Input and Output

#   https://stepik.org/lesson/265077/step/7?unit=246025
# ver_1
print("*")
print("**")
print("***")

print("****")
print("*****")
print("******")
print("*******")

# ver_2
print(*['*'*i for i in range(8)], sep='\n')



#   https://stepik.org/lesson/275252/step/6?unit=256355
# ver_1
name = input()
d = input()
c = input()
b = input()
print(d,c,b, sep=name)

# ver_2
r = input()
print(input(), input(), input(), sep=r)



#   https://stepik.org/lesson/265079/step/9?unit=246027
# ver_1
a = int(input())
print('Следующее за числом', a, 'число:', (a+1))
print('Для числа', a, 'предыдущее число:', (a-1))

# ver_2
a = int(input())
print(f'Следующее за числом {a} число: {a+1}\nДля числа {a} предыдущее число: {a-1}')



#######################################################################################################################
# Chapter 3. Conditional operator


#   https://stepik.org/lesson/265081/step/12?thread=solutions&unit=246029
# ver_1
num1, num2, num3 = int(input()), int(input()), int(input())
counter = 0
if num1 >= 0:
    counter = counter + num1
if num2 >= 0:
    counter = counter + num2
if num3 >= 0:
    counter = counter + num3
print(counter)

# ver_2
a = 0
for i in range(3):
    num = int(input())
    if num > 0:
        a += num
print(a)



#   https://stepik.org/lesson/265083/step/15?thread=solutions&unit=246031
# ver_1
x1, y1, x2, y2=int(input()), int(input()), int(input()), int(input())
if (-1 <= x1 - x2 <= 1) and (-1 <= y1 - y2 <= 1):
    print('YES')
else:
    print('NO')


#   https://stepik.org/lesson/265082/step/6?thread=solutions&unit=246030
# ver_1
a = int(input())
if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
    print (31)
if a == 4 or a == 6 or a == 9 or a == 11:
    print (30)
elif a == 2:
    print (28)

# ver_2
a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(a[int(input())-1])


#   https://stepik.org/lesson/265082/step/11?unit=246030
# ver_1
a1, a2, b1, b2 = int(input()), int(input()), int(input()), int(input()),
if a1 < b1 and a2 > b2 or a1==b1 and a2==b2:      #    3, 9
    print (b1, b2)
elif b1 < a1 and b2 > a2 or b1==a1 and b2==a2:      #    6, 9 наоборот
    print (a1, a2)
elif a2==b1 and a1 < a2:                            #    7
    print (a2)
elif b2==a1 and b1 < b2:                            #    8
    print (b2)
elif a1 < b1 < a2:                           #    4
    print (b1, a2)
elif b1 < a1 < b2:                                  #    5
    print (a1, b2)
elif a1==b1 and a2 < b2 or b1 < a1 and b2==a2:      #    10, 11
    print (a1, a2)
elif a1 > b1 and a2==b2 or b1==a1 and b2<a2:        #    12, 13
    print (b1, b2)
elif a2 < b1 or b2 < a1:                              #    1, 2
    print ('пустое множество')

# ver_2
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

a, b = max(a1, a2), min(b1, b2)
if a == b:
    print(a)
elif a > b:
    print('пустое множество')
else:
    print(a, b)


#######################################################################################################################
# Chapter 3. Data types


#   https://stepik.org/lesson/265105/step/13?unit=246053
# ver_1
a, b, c = input(), input(), input()
print(sorted(map(int, [a, b, c]))[2])
print(sorted(map(int, [a, b, c]))[1])
print(sorted(map(int, [a, b, c]))[0])

# sorted - создает список и сортирует его в порядке возростания
# map - применяет int к переменным
# [2] - третье число в списке
# Этому меня научили ребята из предыдущих уроков. Я просто смотрел решения и спрашивал «как это работает?» Это мои
# первые курсы по програмированию и вообще я сейчас сижу на заводе. Сижу, решаю эти курсы т.к. вся работа уже давно
# сделана, а отсидеть 8 часов надо.
# Всем успехов;)


#   https://stepik.org/lesson/265110/step/7?unit=246058
# ver_1
from math import *
a, b, c = float(input()), float(input()), float(input())
d=(b ** 2) - 4 * a * c
if d < 0:
    print ('Нет корней')
elif d == 0:
    print (-b / (a * 2))
elif d > 0:
    x1 = (-b + sqrt((b ** 2) - 4 * a * c )) / (2 * a)
    x2 = (-b - sqrt((b ** 2) - 4 * a * c )) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))

# ver_2
from math import sqrt   # Зачем нам вся библиотека ???
a, b, c = float(input()), float(input()), float(input())
d=(b ** 2) - 4 * a * c
if d < 0:
    print ('Нет корней')
elif d == 0:
    print (-b / (a * 2))
elif d > 0:
    x1 = (-b + sqrt((b ** 2) - 4 * a * c )) / (2 * a)
    x2 = (-b - sqrt((b ** 2) - 4 * a * c )) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))


#######################################################################################################################
# Chapter 4. For and while loops


#   https://stepik.org/lesson/265118/step/8?unit=246067
# ver_1
a = int(input())
for i in range(a + 1):
    print ('Квадрат числа', i, "равен", i ** 2)

# ver_2
for i in range(int(input())+1):
    print(f'Квадрат числа {i} равен {i**2}')


#   https://stepik.org/lesson/294243/step/15?thread=solutions&unit=275922
# ver_1
n, a, y = int(input()), 1, 0
for i in range(n):
    b=a
    a=b+y
    y=b
    print(b, end=' ')

# ver_2
n, f1, f2 = int(input()), 1, 1
for i in range(n):
    print(f1, end=' ')
    f1, f2 = f2, f1 + f2


#
# ver_1


# ver_2


#
# ver_1


# ver_2


#
# ver_1


# ver_2


#
# ver_1


# ver_2


#
# ver_1


# ver_2
