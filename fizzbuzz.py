import sys

def get_arguments():
    count_number = int(sys.argv[1])
    return count_number

def check_number_validity():
    if not isinstance(count_number, int):
        print("Error: count_number is not a number")
        sys.exit(1)

count_number = get_arguments()
check_number_validity()

print("Running...")

counter = 0
while counter != count_number:
    #switch
    counter += 1
    action_case = 0
    if counter % 3 == 0:
        action_case += 1
    if counter % 5 == 0:
        action_case += 2

    match action_case:
        case 1:
            print("Fizz")
        case 2:
            print("Buzz")
        case 3:
            print("Fizzbuzz")
        case 0:
            print(counter)
print("Exiting.")