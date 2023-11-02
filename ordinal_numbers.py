numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # List of integers
for number in numbers:
    if number == 1:  # Check if the number is 1 not "1"
        print(f"{number}st")  # Print as "1st"
    elif number == 2:  # Check if the number is 2 not "2"
        print(f"{number}nd")  # Print as "2nd"
    elif number == 3:  # Check if the number is 3 not "3"
        print(f"{number}rd")  # Print as "3rd"
    else:
        print(f"{number}th")  # Print as "4th" to "9th"
