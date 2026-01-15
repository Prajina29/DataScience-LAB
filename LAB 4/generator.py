'''3. Create a generator function using the yield keyword that produces numbers from 1 to 5
 one by one to illustrate how lazy evaluation can save memory when dealing with large
datasets.'''

def number_generator():
    for i in range(1,6):
        yield i # yield keyword gives euta number at a time 

gen = number_generator()

for num in gen:
    print(num)