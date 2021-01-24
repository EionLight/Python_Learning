try:
    z=int(input("Enter the Year"))
    y=2020-z
    print("The Age is",y)
except ValueError:
    print("Please enter Correct Year in correct format")