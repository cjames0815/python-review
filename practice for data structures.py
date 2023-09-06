# Initialize a dictionary to store the counts of each integer
count_dict = {}

# Prompt the user for input
while True:
    try:
        num = int(input("Enter an integer between 1 and 10 (or any other number to stop): "))
        if 1 <= num <= 10:
# Increment the count of the entered integer
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        else:
            break  # Stop the loop if the input is outside the range
    except ValueError:
        break  # Stop the loop if the input is not a valid integer

# Print the counts of each integer
for num, count in count_dict.items():
    if count == 1:
        print(f"{num} appears {count} time")
    else:
        print(f"{num} appears {count} times")



