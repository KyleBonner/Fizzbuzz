import sys

def get_arguments():
    count_number = sys.argv[1]
    return count_number

def check_number_validity():
    if count_number.isdigit() is not True:
        print("error: The number is not valid")
        sys.exit(1)

count_number = get_arguments()
check_number_validity()