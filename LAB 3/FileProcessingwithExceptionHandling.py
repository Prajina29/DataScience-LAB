# 2. File Processing with Exception Handling
# ● Reads numbers from a text file (one number per line)
# ● Ignores invalid entries using exception handling
# ● Calculates and displays the sum and average of valid numbers

f = open("numbers.txt", "w")
f.write("20 bjhb\n")
f.write("abcd\n")
f.write("efgh\n")
f.write("30\n")
f.write("80\n")
f.close()
try:
    f=open("numbers.txt","r")
    total=0
    count=0

    for line in f:
        try:
            num = int(line)
            total += num
            count += 1
        except ValueError:
            continue

    f.close()

    if count > 0:
        average = total / count
        print("Sum =", total)
        print("Average =", average)
    else:
        print("No valid numbers found")

except FileNotFoundError:
    print("File not found")