from platform import java_ver
from random import randint
from cmath import sqrt
import random 
import math
from tkinter import N
from traceback import print_tb
from unittest import result

# 0 Вывести квадрат числа

# a = int(input()) 
# b = a**2
# print(b)

# 1.По двум заданным числам проверять является ли первое квадратом второго

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# c = a == b*b
# print(c)
# 2.Даны два числа. Показать большее и меньшее число

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# if a > b:
#     print(f'{a} больше {b}')
# else:
#     print(f'{b} больше {a}')       

# 3.По заданному номеру дня недели вывести его название
# Можно же лучше 
# day_of_week = ['пн','вт','ср','чт','пт','сб','вс']
# day_numb = [1,2,3,4,5,6,7,8]
# day = int(input('Введите число: '))

# if day == day_numb[0]:
#     print(day_of_week[0])
# elif day == day_numb[1]:
#     print(day_of_week[1])    
# elif day == day_numb[2]:
#     print(day_of_week[2])
# elif day == day_numb[3]:
#     print(day_of_week[3])
# elif day == day_numb[4]:
#     print(day_of_week[4])
# elif day == day_numb[5]:
#     print(day_of_week[5])
# elif day == day_numb[6]:
#     print(day_of_week[6])

# 4.Найти максимальное из трех чисел

# def max(a,b,c):
#     mx = a
#     if b > mx:
#         mx = b
#     if c > mx:
#         mx = c
#     print(f'максимальное {mx}')
# max(int(input('первое:')),int(input('второе:')),int(input('третье:')))                  

# 5.Написать программу вычисления значения функции y = f(a)

# import math          

# def sin(a):
#     print(math.sin(a))
# sin(10)

#6.Выяснить является ли число чётным

# a = float(input('Введите число: '))
# def even_numb(numb):
#     res = numb % 2 == 0
#     print(res)
# even_numb(a)

#7. Показать числа от -N до N

# numb_a = int(input('от '))
# numb_b = int(input('до '))
# ran = range(numb_a, numb_b+1)
# numbers = list(ran)
# print(numbers)

#8. Показать четные числа от 1 до N

# numb = int(input('до '))
# ran = range(0, numb+1, 2)
# numbers = list(ran)
# print(numbers)

#9. Показать последнюю цифру трёхзначного числа

# def last_number(a):
#     return a % 10
# print(last_number(145))

#10. Показать вторую цифру трёхзначного числа

# def second_number(a):
#     return a % 100 // 10
# number = int(input('Введите число: '))
# print(second_number(number))

#11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

# numbers = random.randint(10,99+1)
# print(numbers)
# def max_numb(num):
#     if num // 10 > num % 10:
#         return num // 10
#     else:
#         return num  % 10
# print()
# print(max_numb(numbers))   

#12.Удалить вторую цифру трёхзначного числа

# number = int(input('Введите число: '))
# def dell_numb(numb):
#     first = numb // 100
#     last = numb % 10
#     return first * 10 + last
# print(dell_numb(number))

#13.Выяснить, кратно ли число заданному, если нет, вывести остаток.
# number_one = int(input('Введите число: '))
# number_two = int(input('Введите число: '))

# def multip(numb_1, numb_2):
#     if numb_1 % numb_2 == 0:
#         print('Ok')
#     else:
#         print(numb_1 % numb_2)
# multip(number_one, number_two)

#14.Найти третью цифру числа или сообщить, что её нет
# number = int(input('Введите число: '))

# def find_numb_3(numb):
#     if 1000 > numb > 100:
#         return print(numb % 10)
#     elif numb > 1000:
#         return print((numb % 100) // 10)  
#     else:
#         return print('not found')

# find_numb_3(number)

#15.Дано число. Проверить кратно ли оно 7 и 23

# number = int(input('Введите число: '))
# number = random.randint(1,1000)
# def multip_1(numb):
#     return numb % 7 == 0 and numb % 23 == 0

# print(number)
# print(multip_1(number))

#16. Дано число обозначающее день недели. Выяснить является номер дня недели выходным 

# day_week = int(input('Введите число: '))

# def weekend(numb):
#     return numb == 6 or numb == 7

# print(weekend(day_week))

#17.По двум заданным числам проверять является ли одно квадратом другого

# number_1 = int(input('Введите число: '))
# number_2 = int(input('Введите число: '))

# def sqr_number(numb_1, numb_2):
#     return number_1 == number_2 ** 2 or number_2 == number_1 **2

# print(sqr_number(number_1, number_2))

#18.Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

# def bool(x,y):
#     return not(x or y) == (not x and not y)

# print(bool(0,1))
# print(bool(1,1))
# print(bool(1,0))
# print(bool(0,0))

#19.Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0

# def find_quarter(x,y):
#     if x > 0 and y > 0:
#         return 1
#     elif x < 0 and y >0:
#         return 2
#     elif x < 0 and y < 0:
#         return 3
#     else:
#         return 4

# print(find_quarter(-2,5))

# 20. Задать номер четверти, показать диапазоны для возможных координат

# def quarter(q):
#     if q == 1:
#         print('x > 0, y > 0')
#     elif q == 2:
#         print('x < 0, y > 0')
#     elif q == 3:
#         print('x < 0, y < 0')
#     elif q == 4:
#         print('x > 0, y < 0')

# quarter(2)

#21.Программа проверяет пятизначное число на палиндромом.

# def check_palindrom(numb):
#     return (numb // 10000) % 10 == numb % 10 and (numb // 1000) % 10 == (numb // 10) % 10

# value = int(input('Введите число: '))
# print(check_palindrom(value))

#22.Найти расстояние между точками в пространстве 2D/3D

# sqrt(xb-xa)^2 + (yb - ya)^2
# def find_dist_2D(x1, y1, x2, y2):
#     return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# def find_dist_3D(x1, y1, z1, x2, y2, z2):
#     return sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

# print(find_dist_3D(2,-2,4,8,7,10))
# print(find_dist_2D(2,8,-2,7))

#23.Показать таблицу квадратов чисел от 1 до N
 
# def pow2(number):
#     value = range(1, number+1)
#     for i in value:
#          print(f'{i}^2 = {int(i**2)}')

# pow2(28)

#24.Найти кубы чисел от 1 до N

# def pow3(number):
#     value = range(1,number+1)
#     for i in value:
#         print(f'{i}^3 = {int(i**3)} ')

# pow3(8)

#25.Найти сумму чисел от 1 до А

# def summ(A):
#     sum1 = 0
#     value = range(1, A+1)
#     for i in value:
#         sum1 = sum1 + i
#     print(sum1)

# summ(1997)

#26.Возведите число А в натуральную степень B используя цикл

# def a_pow(a,b):
#     res = 1
#     while(b>0):
#         res = res * a
#         b = b - 1
#     print(res)

# a_pow(2,8)

#27. Определить количество цифр в числе
# numb = input('Введите число: ')
# numb = str(123)
# def find_count(val):
#     print(len(val))

# find_count(numb)

#28.Подсчитать сумму цифр в числе

# def digital_sum(n):
#     if n < 10:
#         return n
#     return n % 10 + digital_sum( n // 10)

# number = int(input('Введите число: '))

# print(digital_sum(number))

#29. Написать программу вычисления произведения чисел от 1 до N

# def composition(N):
#     sum1 = 1
#     value = range(1, N+1)
#     for i in value:
#         sum1 = sum1 * i
#         print(sum1)

# number = int(input('Введите число: '))
# composition(number)

#30.Показать кубы чисел, заканчивающихся на четную цифру

# def cube(num1, num2):
#     a = 0
#     for num1 in range(num2):
#         if num1 % 2 == 0:
#             a = num1**3
#             print(a)
#     return a
    
# cube(1,10)

#31.Задать массив из 8 элементов и вывести их на экран 

# arr = [i for i in range(8)]
# print(arr)

#32.Задать массив из 8 элементов, заполненных нулями и единицами вывести их на экран
            
# a = [] 
# n = 8  
# for i in range(n):  
#     new_element = randint(0,1)
#     a.append(new_element)  
    
# print(a)

#33.Задать массив из 12 элементов, заполненных числами из [0,9]. Найти сумму положительных/отрицательных элементов массива

# a = [] 
# n = 12  
# for i in range(n):  
#     new_element = randint(-9,9)
#     a.append(new_element)  
# print(a)

# sum1 = 0
# sum2 = 0

# for i in range(len(a)):
#     if a[i] < 0:
#         sum1 = sum1 + a[i]
#     elif a[i] > 0:
#         sum2 = sum2 + a[i]
# print(sum1)
# print(sum2)

#34.Написать программу замену элементов массива на противоположные

# a = [] 
# n = 12  
# for i in range(n):  
#     new_element = randint(-9,9)
#     a.append(new_element)  
# print(a)

# for i in range(len(a)):          
#     a[i] = -a[i]

# print(a)

#35.Определить, присутствует ли в заданном массиве, некоторое число

# a = [] 
# n = 12  
# for i in range(n):  
#     new_element = randint(-9,9)
#     a.append(new_element)  
# print(a)

# x = int(input('Введите число: '))

# def find_x(array):
#     for i in range(len(array)):
#         if array[i] == x:
#             print('+')
#             break

# find_x(a)

#36. Задать массив, заполнить случайными положительными трёхзначными числами. Показать количество нечетных\четных чисел

# a = [] 
# n = 10  
# for i in range(n):  
#     new_element = randint(100,1000)
#     a.append(new_element)  
# print(a)


# def even(array):
#     b = 0
#     c = 0
#     for i in range(len(array)):
#         if a[i] % 2 == 0:
#             b = b + 1
#         elif a[i] % 2 != 0:
#             c = c + 1
#     return print(f'нечет {c} четн {b}')

# even(a)

# a = [0]*10
# def fill_array(array, min, max,lens):
#     array = [0]*lens
#     for i in range(len(array)):
#         array[i] = randint(min,max)
#     return array

# a = None
# print(fill_array(a,1,10,10))

#37.В одномерном массиве из 123 чисел найти количество элементов из отрезка [10,99]

###### Для индексов #######
# def fill_array(min, max,lens):
#     array = [0]*lens
#     for i in range(len(array)):
#         array[i] = randint(min,max)
#     return array

# a = fill_array(10,1000,123)  
# print(a) 

# def print_count(array):
#     count = 0
#     for i in array:
#         if i >= 10 and i <= 99:
#             count = count + 1
#     return count

# print(print_count(a))

####### Для значений эл-тов ########
# def fill_array(min, max,lens):
#     array = [0]*lens
#     for i in range(len(array)):
#         array[i] = randint(min,max)
#     return array

# a = fill_array(1,12,10)  
# print(a) 

# def print_count(array):
#     count = 0
#     for i in range(len(array)):
#         if 3 <= array[i] <= 6:
#             count = count + 1
#     return count

# print(print_count(a))

# 38. Найти сумму чисел одномерного массива стоящих на нечетной позиции

# a = fill_array(1,10,13)
# print(a)
# def summ_el(array):
#     summ1 = 0
#     for i in range(len(array)):
#         if i % 2 != 0:
#             summ1 = summ1 + array[i]
#     return summ1

# print(summ_el(a))

#39. Найти произведение пар чисел в одномерном массиве. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# def fill_array(min, max,lens):
#     array = [0]*lens
#     for i in range(len(array)):
#         array[i] = randint(min,max)
#     return array

# a = fill_array(1,10,6)  
# print(a)

# def el_composition(array):
#     res = []
#     x = -1
#     for i in range(len(array)):
#         res.append(array[i] * array[x])
#         x -= 1
#         if array[i] == array[x]:
#             break  
#     return res

# print(el_composition(a))

#В Указанном массиве вещественных чисел найдите разницу между максимальным и минимальным элементом

# def fill_array(min, max,lens):
#     array = [0]*lens
#     for i in range(len(array)):
#         array[i] = randint(min,max)
#     return array

# a = fill_array(1,100,10)  
# print(a)

# def min_max(array):
#     max = 0
#     min = array[1]
#     diff = 0
#     for i in range(len(array)):
#         if array[i] > max:
#             max = array[i]
#         elif array[i] < min:
#             min = array[i]
#         diff = max - min
#     return f'max = {max} min = {min} diff = {diff}'

# print(min_max(a))

#41.Выяснить являются ли три числа сторонами треугольника 

# def trian(a,b,c):
#     return a < b +c and b < a + c and c < a + b

# print(trian(6,2,5))

#42.Определить сколько чисел больше 0 введено с клавиатуры

def find_numbers(value):
    count = 0
    for i in range(len(value)):
        if value[i] != 0:
            count += 1
    return count

number = input('Число: ')
print(find_numbers(number))



        













        


