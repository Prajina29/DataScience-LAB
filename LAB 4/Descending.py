'''Write a Python script that takes a list of student marks and sorts them in descending
order (highest to lowest) using either the sorted() function or the .sort() method.'''


marks = list(map(int, input("Enter student marks separated by space: ").split()))

marks.sort(reverse=True)

print("Marks in descending order:", marks)
