'''
Напишите программу, которая считывает с клавиатуры два числа aa и bb, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b][a;b], которые кратны числу 33.

В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [-5; 12][−5;12]. Всего чисел, делящихся на 33, на этом отрезке 66: -3, 0, 3, 6, 9, 12−3,0,3,6,9,12. Их среднее арифметическое равно 4.54.5

На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 33.﻿
'''
a = -5
b = 12
'''
a = int(input())
b = int(input())
'''
'''
s = 0
for i in range(a,b+1):
	if i % 3 == 0:
		num = i + 1
	s = i
	print(s)
'''
num = 0
s = 0
for i in range(a,b+1):
	if i % 3 == 0:
		s = s + i
		num +=1
print(num)
print(s)

print(s/num)