largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        ii = int(num)
    except:
        print("Invalid input")
    try:
        if largest < ii:
            largest = ii
        if smallest > ii:
            smallest = ii
    except:
        largest = ii
        smallest = ii

print("Maximum is", largest)
print("Minimum is", smallest)