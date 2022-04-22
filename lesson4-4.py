#4. Представлен список чисел. Определите элементы
# списка, не имеющие повторений. Сформируйте итоговый массив чисел,
# соответствующих требованию. Элементы выведите в порядке их
# следования в исходном списке. Для выполнения задания обязательно
# используйте генератор. Пример исходного списка:
# [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]
from random import randint

my_list = [randint(-10, 10) for _ in range(20)] #randint-формируем список диапазон от -10 до 10 в диапазоне 20
uniq_list = [el for  el in my_list if my_list.count(el) == 1] #count  забирает элемент если он входит в структуру my_list один раз
print(f'Source list\n{my_list}\nNo repetition list\n{uniq_list}')

print('*'*100)

print(a := [randint(0,9) for _ in  range(20)], [i for  i in a if a.count(i) == 1], sep="\n")
#:=-оператор морж, присваивает переменной какок-либо значение или постоянно получать или использовать в процессе.
# переменной а присвоено значение [randint(0,9) for _ in  range(20)] и
#:= этот оператор позволяем оспользовать переменную а в a.count(i) == 1

print('*'*100)

my_dict = {i: 0 for i in  my_list}# забираем в ключи значения, пока 0
for i in my_list: #перебрать все элементы списка my_list
    my_dict[i] +=1 # если такой ключ есть то увеличиваем на 1, посчитаем кол-во элементов в списке и отобразим через словарь

print([i for i in my_dict if my_dict[i] ==1]) #потом сформируем список и выведем те ключи у которых значения =1