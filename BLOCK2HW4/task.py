"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго
множества. Затем пользователь вводит сами элементы множеств.

Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод —
на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из
управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь
непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход
собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
"""
import random

def task22():
  size_First_List = int(input("Enter the size of your first list: "))
  first_List = [int(input()) for _ in range(size_First_List)] 
  size_Second_List = int(input("Enter the size of your second list: "))
  second_List = [int(input()) for _ in range(size_Second_List)] 
  print(f'Your First_List:\t\t {first_List}')
  print(f'Your Second_List:\t\t {second_List}')
  sort_Unique_List = sorted(list(set(first_List).union(set(second_List))))
  print(f'Your sorted unique numbers:\t {sort_Unique_List}')

def task24():
  number_Bushes = int(input("Enter the number of bushes: "))
  bushes_List = [int(random.randint(0,30)) for _ in range(number_Bushes)] 
  print(f'Your bushes_List:\t\t {bushes_List}')
  module_Features = 3
  max_Berries = sum(bushes_List[:module_Features])
  temp_Berries = max_Berries
  size_List = len(bushes_List)
  trigger = False
  if len(bushes_List) <= module_Features:
    print(f'The maximum number of berries collected by the module is: {sum(bushes_List)}')
  else:
    for i in range(size_List):
      if i >= size_List-module_Features:
        trigger = True
      circular_Index = module_Features+i-size_List*(int(trigger))
      temp_Berries += bushes_List[circular_Index] - bushes_List[i]
      if temp_Berries > max_Berries:
        max_Berries = temp_Berries
  print (max_Berries)
  

task22()
task24()