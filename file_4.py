# Представлен список чисел. Необходимо вывести те его элементы,
# значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# Подсказка: использовать возможности python, изученные на уроке.
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
from time import perf_counter
import sys
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
start=perf_counter()
result=[src[i] for i in range(1,len(src)) if src[i]>src[i-1]]
print(result,sys.getsizeof(result),perf_counter()-start)
start=perf_counter()
result=(src[i] for i in range(1,len(src)) if src[i]>src[i-1])
print(list(result),sys.getsizeof(result),perf_counter()-start)
#Ответ очевиден, быстрее через генератор и трэба меньше памяти.