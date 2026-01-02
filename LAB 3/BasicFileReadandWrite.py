# 1. Basic File Read & Write
# ● Create a text file and write multiple lines into it
# ● Read the contents of the file and display them on the screen
# ● Handle the case where the file does not exist using try-except

f = open("datas.txt", "w")
f.write("Hello\n")
f.write("How are you?\n")
f.write("I hope you are fine.\n")
f.close()

try:
    f = open("datas.txt", "r")
    data = f.read()
    print(data)
    f.close()
except FileNotFoundError:
    print("File not found")
