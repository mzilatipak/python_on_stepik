# # -*- coding: utf-8 -*-
# 11.1...
# 1. На вход программе подается одно число n. Напишите программу, которая выводит список [1, 2, 3, ..., n].
# n = int(input())
# lst = list(range(1,n+1))
# print(lst)
# 2. На вход программе подается одно число n. Напишите программу,
# которая выводит список, состоящий из n букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.
# n = int(input())
# lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(lst[:n])
# переворот списка (строки)
# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# languages = languages[::-1]
# print(languages)
# 11.3.1
# Дополните приведенный код, чтобы он:
# 1 Вывел длину списка;
# 2 Вывел последний элемент списка;
# 3 Вывел список в обратном порядке (вспоминаем срезы);
# 4 Вывел YES если список содержит числа 5 и 17, и NO в противном случае;
# 5 Вывел список с удаленным первым и последним элементами.
# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# if 5 and 17 in numbers:
#     print("YES")
# else:
#     print("NO")
# del numbers[0]
# del numbers[-1]
# print(numbers)
# 11.3.2
# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая создает из указанных строк список и выводит его.
# n = 3
# # n = int(input())
# spisok = []
# for i in range(n):
#     s = input()
#     spisok.append(s)
# print(spisok)
# 11.3.3
# Напишите программу, выводящую следующий список:
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
# Примечание. Последний элемент списка состоит из 26 символов z.
# list = []
# for i in range(26):
#     list.append(chr(ord('a') + i) * (i + 1))
# print(list)
# 11.3.4
# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список их кубов.
# n = 5
# # n = int(input())
# lst = []
# for i in range (1, n + 1):
#     num = int(input())
#     num **= 3
#     lst.append(num)
# print(lst)
# 11.3.5
# На вход программе подается натуральное число n.
# Напишите программу, которая создает список состоящий из делителей введенного числа.
# n = 17
# # n = int(input())
# lst = []
# for i in range (1, n + 1):
#     if n % i == 0:
#         lst.append(i)
# print(lst)
# 11.3.6
# На вход программе подается натуральное число n≥2, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список,
# состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).
# n = 5
# # n = int(input())
# tmp = int(input())
# lst = []
# for i in range (n-1):
#     num = int(input())
#     lst.append(tmp + num)
#     tmp = num
# print(lst)
# 11.3.7
# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список,
# затем удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.
# n = 5
# # n = int(input())
# lst = []
# for i in range (n):
#     num = int(input())
#     lst.append(num)
# del lst[1::2]
# print(lst)
# 11.3.8**
# На вход программе подается натуральное число n и n строк, а затем число k.
# Напишите программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов.
# Примечание. Если некоторые строки слишком короткие, и в них нет символа с заданным номером,
# то такие строки при выводе нужно игнорировать.
# num = int(input())
# lst = []              # создаём список для последующего наполнения
# for _ in range(num):
#     str1 = input()
#     lst.append(str1)  # наполняем список lst
# k = int(input())   # вводим номер буквы под индексом
# for i in lst[:]:      # обрабатываем список lst
#     if len(i) >= k:   # по условию отбираем зyfчения не меньше k
#         print(i[k - 1], end='')  # печатаем букву под индексом k -1
# 11.3.9
# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая создает список из символов всех строк, а затем выводит его.
# n = int(input())
# lst = []
# for _ in range(n):
#     string = input()
#     lst.extend(string)
# print(lst)
# 11.4.1
# Дополните приведенный код, так чтобы он вывел сумму квадратов элементов списка numbers.
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lst = []
# for num in numbers:
#     lst.append(num * num)
# print(sum(lst))
# 11.4.2
# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая для каждого введенного числа x выводит значение функции
# f(x) = x**2 + 2x + 1, каждое на отдельной строке.
# Примечание. Для первого теста имеем:
# f(1) = 1**2 + 2*1 + 1 = 4, f(2) = 2**2 + 2*2 + 1 = 9, f(3) = 3**2 + 2*3 + 1 = 16, и тд...
# n = int(input())
# lst_x = []
# lst_f = []
# func = 0
# for _ in range(n):
#     x = int(input())
#     lst_x.append(x)
# print(*lst_x, sep='\n')
# print()
# for i in range(n):
#     func = lst_x[i] ** 2 + 2 * lst_x[i] + 1
#     lst_f.append(func)
# print(*lst_f, sep='\n')
# 11.4.3
# При анализе данных, собранных в рамках научного эксперимента,
# бывает полезно удалить самое большое и самое маленькое значение.
# На вход программе подается натуральное число n, а затем n различных натуральных чисел.
# Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел,
# а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.
# n = int(input())
# tmp = []
# lst = []
# for _ in range(n):
#     num = int(input())
#     tmp.append(num)
# for i in tmp:
#     if i != min(tmp) and i != max(tmp):
#         lst.append(i)
# print(*lst, sep='\n')
# 11.4.4
# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.
# n = int(input())
# lst = []
# for _ in range(n):
#     str = input()
#     if str not in lst:
#         lst.append(str)
# print(*lst, sep='\n')
# 11.4.5
# На вход программе подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос.
# Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.
# n = int(input())
# lst = []
# tmp = []
# for _ in range(n):
#     str = input()
#     tmp.append(str)
# req = input()
# for i in range(len(tmp)):
#     if req.lower() in tmp[i].lower():
#         lst.append(tmp[i])
# print(*lst, sep='\n')

# 11.4.6**
""" # На вход программе подается натуральное число n, затем n строк,
# затем число k — количество поисковых запросов,
# затем k строк — поисковые запросы.
# Напишите программу, которая выводит все введенные строки,
# в которых встречаются все поисковые запросы.
n = int(input())
str_lst = []
req_lst = []

for _ in range(n):
    str = input()  # вводим строки
    str_lst.append(str)  # список строк

k = int(input())
for _2 in range(k):
    req = input()  # вводим запросы
    req_lst.append(req) # список запросов

# ищем запросы в строках
for i in str_lst:
    count = 0  # счётчик совпадений
    for j in req_lst:  # сравниваем наличией элемента из списка поиска с основным
        if j.lower() in i.lower():  # если совпадение найдено:
            count += 1
    if count == len(req_lst):  # если счётчик совпадений равен или больше количеству элементов поискового списка, 
        # печатаем элемент из основного списка.
        print(i) """

# 11.4.7
# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая сначала выводит все отрицательные числа,
# затем нули, а затем все положительные числа, каждое на отдельной строке.
# Числа должны быть выведены в том же порядке, в котором они были введены.
# n = int(input())
# minus = []
# zero = []
# plus = []
# for _ in range(n):
#     nmb = int(input())
#     if nmb < 0:
#         minus.append(nmb)
#     elif nmb == 0:
#         zero.append(nmb)
#     elif nmb > 0:
#         plus.append(nmb)
# print(*minus, *zero, *plus, sep='\n')
# 11.5.1
# На вход программе подается строка текста.
# Напишите программу, которая выводит слова введенной строки в столбик.
# str = 'У лукоморья дуб зеленый златая цепь на дубе том'
# #str = input()
# print(*str.split(), sep='\n')
# 11.5.2
# На вход программе подается строка текста, содержащая имя, отчество и фамилию человека.
# Напишите программу, которая выводит инициалы человека.
# str = 'Владимир Семенович Высоцкий'
# #str = input()
# lst = str.split()
# for i in range(len(lst)):
#     print(lst[i][0], end='.')
# 11.5.3
# В операционной системе Windows полное имя файла состоит из буквы диска,
# после которого ставится двоеточие и символ  "\",
# затем через такой же символ перечисляются подкаталоги (папки),
# в которых находится файл, в конце пишется имя файла (C:\Windows\System32\calc.exe).
# На вход программе подается одна строка с корректным именем файла в операционной системе Windows.
# Напишите программу, которая разбирает строку на части, разделенные символом "\".
# Каждую часть вывести в отдельной строке.
# str = 'C:\Windows\System32\calc.exe'
# #str = input()
# print(*str.split('\\'), sep='\n')
# 11.5.3
# На вход программе подается строка текста, содержащая целые числа.
# Напишите программу, которая по заданным числам строит столбчатую диаграмму.
# num = '5 3 1 7 10 2'
# # num = int(input())
# lst = num.split()
# for i in range(len(lst)):
#     # num[i] = int(num[i])  # преобразование эл-тов списка в числа
#     print('+' * int(lst[i]))
# 11.5.4
# На вход программе подается строка текста, содержащая 4 целых положительных числа, разделенных точкой.
# Напишите программу, которая определяет, является ли введенная строка текста корректным ip-адресом.
# Примечание. ip-адрес является корректным, если все 4 числа находятся в диапазоне от 0 до 255 включительно.
# ip1 = '192.168.0.3'
# ip2 = '192.168.0.300'
# # ip = input()
# lst = ip1.split('.')
# count = 0
# for i in range(len(lst)):
#     if int(lst[i]) in range(0, 255):
#         count += 1
# if count == 4:
#     print("ДА")
# else:
#     print("НЕТ")
# 11.5.5
# На вход программе подается строка текста и строка-разделитель.
# Напишите программу, которая вставляет указанный разделитель между каждым символом введенной строки текста.
# str = '1234567'
# razd = '*'
# # str = input()
# # razd = input()
# print(razd.join(str))
# 11.5.6
# На вход программе подается строка текста, содержащая натуральные числа.
# Из данной строки формируется список чисел.
# Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# str = '3 3 3 3 3'
# # str = int(input())
# count = 0
# lst = str.split()
# print(lst)
# for i in range(len(lst)):
#     for k in range(i + 1, len(lst)):
#         if lst[i] == lst[k]:
#             count += 1
# print(count)
# 11.6.1
# Дополните приведенный код, чтобы он:
# 1 Заменил второй элемент списка на 17;
# 2 Добавил числа 4, 5 и 6 в конец списка;
# 3 Удалил первый элемент списка;
# 4 Удвоил список;
# 5 Вставил число 25 по индексу 3;
# Вывел список, с помощью функции print()
# numbers = [8, 9, 10, 11]
# numbers[1] = 17  # 1
# numbers.append(4)  # 2
# numbers.append(5)  # 2
# numbers.append(6)  # 2
# numbers.pop(0)  # 3
# numbers *= 2 # 4
# numbers.insert(3, 25)  # 5
# print(numbers)
# 11.6.2
# На вход программе подается строка текста, содержащая различные натуральные числа.
# Из данной строки формируется список чисел.
# Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.
# Примечание. Используйте подходящие встроенные функции и списочные методы.
# numbers = '3 4 5 2 1'
# lst = []
# # numbers = input()
# lst = numbers.split()
# for i in range(len(lst)):
#     lst[i] = int(lst[i])
# print(lst)
# mnm = min(lst)
# mxm = max(lst)
# pos_mnm = lst.index(mnm)
# pos_mxm = lst.index(mxm)
# lst[pos_mnm] = mxm
# lst[pos_mxm] = mnm
# print(*lst)
# print('min =', mnm, ', max =', mxm)
# print('pos min =', pos_mnm, ', pos max =', pos_mxm)
# 11.6.3
# На вход программе подается строка, содержащая английский текст.
# Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.
# Примечание. Артикли могут начинаться с заглавной буквы 'A', 'An', 'The'.
# str = 'William Shakespeare was born in the town of Stratford, England, in the year 1564.' \
#       ' When he was a young man, Shakespeare moved to the city of London, where he began writing plays. ' \
#       'His plays were soon very successful, ' \
#       'and were enjoyed both by the common people of London and also by the rich and famous. ' \
#       'In addition to his plays, Shakespeare wrote many short poems and a few longer poems. ' \
#       'Like his plays, these poems are still famous today.'
# # str = input().lower()
# lst = str.split()
# count_a = lst.count('a')
# count_an = lst.count('an')
# count_the = lst.count('the')
# print('Общее количество артиклей:', count_a + count_an + count_the)
# 11.6.4 *
# Немалоизвестный в пустошах Мохаве Курьер забрел в Хидден-Вэли – секретный бункер Братства Стали
# и любезно соглашается помочь им в решении их проблем.
# Одной из такой проблем являлся странный компьютерный вирус,
# который проявлялся в виде появления комментариев к программам на терминалах Братства Стали.
# Известно, что программисты Братства никогда не оставляют комментарии к коду и пишут программы на Python,
# поэтому удаление всех этих комментариев никак не навредит им.
# Помогите писцу Ибсену удалить все комментарии из программы.
# Формат входных данных. На первой строке вводится символ решётки и сразу же натуральное число n
# — количество строк в программе, не считая первой.
# Далее следует n строк кода.
# Пример:
# name = input()
# print("Введите пароль, если имеется")    # ахахахах вам не поймать меня
# inp = input().split('#')
# n = int(inp[1])
# lst = []
# for _ in range(n):
#         str = input()
#         if str.find('#') > -1:  # если в строке есть решётка, значит это та строка где надо удалить хакерский коммент
#                 ind = str.find('#')  # нашли индекс начала комментария
#                 str = str[0:ind]  # обрезали комментарии
#         str = str.rstrip()  # обрезал пробелы
#         lst.append(str)  # собрали строки в список
# print(*lst, sep='\n')
# # print(inp, n, lst, sep='\n')
# 11.6.5
# На вход программе подается строка текста, содержащая целые числа.
# Из данной строки формируется список чисел.
# Напишите программу, которая сортирует и выводит данный список сначала по возрастанию, а затем
# str = '4 5 1 2 3 8'
# # str = input()
# lst = str.split()
# int_lst = [int(i) for i in lst]  #Преобразование string в int в списке
# int_lst.sort()
# print(*int_lst)
# int_lst.sort(reverse=True)
# print(*int_lst)
# 11.7.5
# На вход программе подается натуральное число n.
# Напишите программу, использующую списочное выражение, которая создает список,
# содержащий квадраты чисел от 1 до n (включительно),
# а затем выводит его элементы построчно, то есть каждый на отдельной строке.
# Примечание. Для вывода элементов списка используйте цикл for.
# n = int(input())
# lst = [i ** 2 for i in range(1, n+1)]
# lst = [i ** 2 for i in range(1, int(input()+1))]
# print(*lst, sep='\n')
# 11.7.6
# На вход программе подается строка текста, содержащая целые числа.
# Напишите программу, использующую списочное выражение,
# которая выведет кубы указанных чисел также на одной строке.
# Примечание 1. Для вывода элементов списка используйте цикл for.
# Примечание 2. Используйте метод split().
# tmp = [int(num) for num in input().split()]
# lst = [tmp[i] ** 3 for i in range(len(tmp))]
# print(*lst)
# 11.7.7
# На вход программе подается строка текста, содержащая слова.
# Напишите программу, которая выводит слова введенной строки в столбик.
# Примечание. Программу можно написать в одну строку кода.
# print(*input().split(), sep='\n')
# 11.7.8
# На вход программе подается строка текста.
# Напишите программу, использующую списочное выражение,
# которая выводит все цифровые символы данной строки.
# Примечание. Программу можно написать в одну строку кода.
# print(*[num for num in input() if num in '1234567890'], sep='')  #v1
# print(*[num for num in input() if num.isdigit()], sep='')  #v2
# 11.7.9
# На вход программе подается строка текста, содержащая целые числа.
# Напишите программу, использующую списочное выражение,
# которая выводит не оканчивающиеся на цифру 4 квадраты четных чисел.
# Примечание. Программу можно написать в одну строку кода.
# print(*[int(i) ** 2 for i in input().split() if int(i) ** 2 % 2 == 0 and int(i) ** 2 % 10 != 4])
# Выводим распакованный список *[преобразуем в числовой формат переменную цикла int(i)
# возводим в степень ** 2 создаем цикл пропускающий элементы списка
# for i in input().split() условие если преобразованная в формат числа переменная цикла возведенная в квадрат,
# деленная на 2, не имеет остатка и деленная на 10 не заканчивается на 4
# if int(i) ** 2 % 2 == 0 and int(i) ** 2 % 10 != 4 ] закрыли список
# 11.8.1 пузырьковая сортировка, оптимизация
# a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97,
#      -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0,
#      -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63,
#      -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]
#
# n = len(a)
# swap = True  # задаём сигнальную метку
#
# for i in range(n - 1):
#
#     if swap == False:  # если по окончании внешнего цикла сигнальная метка приняла значение False,
#         # т.е. ни одного обмена не было произведено, тогда программа прерывается
#         break
#
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#
#             swap = True  # если в данном внутреннем цикле была произведена хотя бы одна перестановка во внутреннем цикле
#             # сигнальная метка принимает значение True
#         else:
#             False  # если в данном внутреннем цикле не было произведено ни одной перестановки,
#             # сигнальная метка сохраняет значение False
#
# print(a)
# 11.8.2 сортировка выбором
# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
# n = len(a)
# for i in range(0, n-1):  # итерируемся по массиву
#     mn = i  # инициализируем минимальный индекс
#     for j in range(i + 1, n):  # итерируемся по оставшимся элементам массива
#         if a[j] < a[mn]:  # проверяем, если j-тое значение меньше текушего минимального
#             mn = j # обновляем минимальные значение
#     a[i], a[mn] = a[mn], a[i]  # меняем i-тое и j-тое значения
#
# print(a)
# 12.2.1 exm
# На вход программе подается четное число n, n ≥ 2.
# Напишите программу, которая выводит список четных чисел [2, 4, 6, ..., n].
# n = int(input())
# lst = [i for i in range(1, n+1) if i % 2 == 0]
# print(lst)
# 12.2.2 exm
# На вход программе подаются две строки текста, содержащие целые числа.
# Из данных строк формируются списки чисел L и M.
# Напишите программу, которая создает третий список,
# элементами которого являются суммы соответствующих элементов списков L и M.
# Далее программа должна вывести каждый элемент полученного списка на одной строке через 1 пробел.
# Примечание. Количество чисел в обеих строках одинаковое.
# l = [int(i) for i in input().split()]
# m = [int(i) for i in input().split()]
# final = []
# for i in range(len(l)):
#     final.append(l[i] + m[i])
# print(final)
# 12.2.3 exm
# На вход программе подается строка текста, содержащая натуральные числа.
# Напишите программу, которая вставляет между каждым числом знак +, а затем вычисляет сумму полученных чисел.
# Примечание. Строковый метод join() работает только со списком строк.
# lst = input().split()
# summ = 0
# for i in range(len(lst)):
#     summ += int(lst[i])
# print(*lst, sep='+', end='=')
# print(summ)
# 12.2.4 ** exm **
# На вход программе подается строка текста.
# Напишите программу, которая определяет, является ли введенная строка корректным телефонным номером.
# Строка текста является корректным телефонным номером,
# если она имеет формат: abc-def-hijk или 7-abc-def-hijk,
# где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.
# Примечание. Телефонный номер должен содержать только цифры и символ -,
# а количество цифр в каждой группе должно быть правильным.
# str = '7-301-4477-5820'
# num_lst = input().split('-')
# if len(num_lst) == 4 and num_lst[0] == '7':
#     del num_lst[0]
# if len(num_lst) == 3 \
#     and len(num_lst[0]) == 3 and num_lst[0].isdigit() \
#     and len(num_lst[1]) == 3 and num_lst[1].isdigit() \
#     and len(num_lst[2]) == 4 and num_lst[2].isdigit():
#     print("YES")
# else:
#     print("NO")
# 12.2.5
# На вход программе подается строка текста.
# Напишите программу, использующую списочное выражение,
# которая находит длину самого длинного слова.
#print(max([len(n) for n in input().split()]))
# 12.2.6
# На вход программе подается строка текста. 
# Напишите программу, использующую списочное выражение, 
# которая преобразует каждое слово введенного текста в "молодежный жаргон" по следующему правилу: 
# 1. первая буква каждого слова удаляется и ставится в конец слова; 
# 2. затем в конец слова добавляется слог "ки".
# [print((i+(i[0]+'ки'))[1:],end=' ') for i in input().split()]
