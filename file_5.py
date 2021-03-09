# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
import sys
from time import perf_counter
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start=perf_counter()
new_src=[]
for ln in src:
    if src.count(ln)==1:
        new_src.append(ln)
print(new_src,sys.getsizeof(new_src),perf_counter()-start)
#Самый медленный варик
start=perf_counter()
new_src=[ln for ln in src if src.count(ln)==1]
print(new_src,sys.getsizeof(new_src),perf_counter()-start)
#Опа,а сахарок то быстрее бегает
start=perf_counter()
new_src=(ln for ln in src if src.count(ln)==1)
print(list(new_src),sys.getsizeof(new_src),perf_counter()-start)
#С генератором чуть медленнее,но меньше памяти
my_set_1=set()
my_set_2=set()
start=perf_counter()
for ln in src:
    if ln not in my_set_2:
        my_set_1.add(ln)
    else:my_set_1.discard(ln)
    my_set_2.add(ln)
new_src=[ln for ln in src if ln in my_set_1]
print(new_src,sys.getsizeof(new_src),perf_counter()-start)
start=perf_counter()
new_src=(ln for ln in src if src.count(ln)==1)
print(*new_src,sys.getsizeof(new_src),perf_counter()-start,sep=' ')
#Самый быстрый вариант,но это не список