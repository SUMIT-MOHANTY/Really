def even_generator (limit):
   for i in range(limit):
       if i % 2 == 0:
           yield i

for num in even_generator(10):
    print(num)