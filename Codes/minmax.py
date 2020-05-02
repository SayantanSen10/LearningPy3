largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        if largest is None:
            largest = num
        elif largest < num:
            largest = num
        elif smallest is None:
            smallest = num
        elif smallest > num:
            smallest = num
        else:
            continue
    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
