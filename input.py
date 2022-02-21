# We can use this syntax to take in input from the user
test = input()
print(test)

# We can ask questions to the user in the input form
test = input("Enter the IP: ")
print(test)

while True:
    test = input("Enter the IP: ")
    # This is the format method we learned in a previous method
    print(">>> {}".format(test))

    # This is a condition that makes the loop stop when it is satisfied.
    if test == "exit":
        break
    else:
        print("exploiting...")