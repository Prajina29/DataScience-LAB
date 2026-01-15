"""2. Use a list comprehension to create a new list containing only the even numbers between 1 and 20,
 demonstrating a more concise and readable alternative to traditional loops."""


'''print ("Even numbers between 1 and 20 are :")
for i in range (1, 21):
    if i % 2 == 0:
        print("i")'''


even_numbers = [i for i in range(1,21) if i % 2 == 0]
 
print("Evennumbers are :", even_numbers)