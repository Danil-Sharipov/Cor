from threading import Thread
import math
import time
max = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10
nums = []
for i in range (0, max):
    nums.append(i)
# Решение в одном потоке
print("Один поток")
start = time.time()
temp = sum(map(math.sin,nums))
print(1,time.time() - start,temp)
# Поиск количества потоков в диапазоне от 2 до 40
print("Несколько потоков")
def sin(x):
  return sum(map(math.sin,x))
def split_in_chunk(jobs,max):
  chunk_size = max//jobs
  # chunk_size = max >> 3 
  for i in range(jobs-1):
    yield slice(i*chunk_size,(i+1)*chunk_size)
  else:
    yield slice((i+1)*chunk_size,None)
class TWRV(Thread):
  def __init__(self,target,args):
    super().__init__(target=target,args=args)
    super().start()
  def run(self):
    self._return = self._target(*self._args, **self._kwargs)
  def join(self):
    super().join()
    return self._return
def main(nums, jobs):
  threads = tuple(map(lambda x: TWRV(target=sin,args=(nums[x],)),split_in_chunk(jobs,max)))
  return sum(map(lambda x: x.join(),threads))
def test(jobs):
  start = time.time()
  temp = main(nums,jobs)
  return (time.time() - start, temp)
for i in range(2,40):
  print(i,*test(i))


"""Вычисления на CPU
Один поток
0.26357507705688477 секунды
Несколько потоков
8 потоков 0.2713541603088379
Большие затраты времени идут на распараллеливание задачи и управление потоками 
это видно на профилировании cProfile, еще нагляднее на py-heat
Код изучал с помощью дизассемблера dis, лучшего достигнуть не получилось
Код можно в паре мест улучшить с учетом некой априорной информации
(например, если число потоков это степень числа 2 можно сделать более быструю
команду смещения побитового >> однако это дает незначительный выход)"""
