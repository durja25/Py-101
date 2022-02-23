import sys

# This tells us the version of the module and the version of the Python interpreter
print(sys.version)

# This shows us the current executable binary of Python
print(sys.executable)

# This shows us the platform we're currently running on
print(sys.platform)

# This tells python to accept input
for line in sys.stdin:
    break
    # If the line from user says exit, then it stops
    if line.strip() == "exit":
        break
    # If it does not say exit, it writes onto the CLI. It writes back what
    # the user inserted.
    sys.stdout.write(">> {}".format(line))

for i in range(1, 5):
    # This writes each element of range(1, 5) as a string
    sys.stdout.write(str(i))
    # This flushes out everything in Python at once. Instead of stdout.write printing each
    # element line by line, everything in the buffer/waiting list gets printed in the same line.
    sys.stdout.flush()

for i in range(1, 5):
    print(i)  # This prints out each element in range(1, 5)

# We're gonna use this to make our own status bar based on time
import time

for i in range(0, 51):
    time.sleep(0.1)  # This means sleep 0 second between each element
    sys.stdout.write("{} [{}{}]\r".format(i, '#' * i, "." * (50 - i)))  # I need to find out what \r is in Python.
    # This basically shows our progress and works like a status bar.
    sys.stdout.flush()
sys.stdout.write("\n")

print(sys.argv)  # This gives us a list of command line arguments which were passed to the script. The first element
# will always be the name of the script.

# We can give out errors if input criterion are not fulfilled using sys.
if len(sys.argv) != 3:
    # The name of the script is always
    # going to be sys.argv[0]
    print("[X] To run {} enter a username and password".format(sys.argv[0]))

    # This shows the type of exit there will be from the script if this condition is met.
    sys.exit(5)

# If we're looking for data from the user from the command line, we can assign the data its
# own name in advance using sys
username = sys.argv[1]
password = sys.argv[2]

print("{} {}".format(username, password))  # We can now access the username and password aside from the sys.argv

print(sys.path)  # sys can shows us the path we are working on.
print(sys.modules)  # sys shows us all the modules we currently have access to


sys.exit(0) # If nothing else along the way breaks, sys will use this code to exit the script


# Resource [sys](https://docs.python.org/3/library/sys.html)