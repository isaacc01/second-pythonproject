#Q1

def max_num(num1, num2, num3):
    # Compare the first two numbers to find the maximum
    max_value = max(num1, num2)
    
    # Compare the maximum of the first two numbers with the third number
    max_value = max(max_value, num3)
    
    return max_value

# Test the function with some values
num1 = 10
num2 = 5
num3 = 8

result = max_num(num1, num2, num3)
print(f"The maximum number is: {result}")


def mult_num(2, 4, 6, 8):
    max_value = max()

# Q2

def mult_list(numbers):
    # Initialize the product to 1
    product = 1
    
    # Iterate through the list and multiply each number with the product
    for num in numbers:
        product *= num
    
    return product

# Test the function with a list of numbers
num_list = [2, 3, 4, 5]
result = mult_list(num_list)
print(f"The product of the numbers in the list is: {result}")

# Q3

def rev_string(input_string):
    # Use slicing to reverse the string
    reversed_string = input_string[::-1]
    
    return reversed_string

# Test the function with a string
original_string = "Hello, World!"
reversed_result = rev_string(original_string)
print(f"The reversed string is: {reversed_result}")


# Q4

def num_within(number, start_range, end_range):
    # Check if the number is greater than or equal to the start of the range
    # and less than or equal to the end of the range
    if start_range <= number <= end_range:
        return True
    else:
        return False

# Test the function with examples
print(num_within(3, 2, 4))  # True
print(num_within(3, 1, 3))  # True
print(num_within(10, 2, 5)) # False

# Q5

def pascal(n):
    # Initialize an empty list to store the rows of Pascal's triangle
    triangle = []

    for i in range(n):
        # Initialize a list for the current row
        row = [1]  # The first element in every row is 1

        # Calculate the elements in the current row based on the previous row
        if triangle:
            prev_row = triangle[-1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])

            row.append(1)  # The last element in every row is also 1

        triangle.append(row)

    # Print Pascal's triangle
    for row in triangle:
        print(' '.join(map(str, row)).center(n * 3))

# Test the function with n = 5
n = 5
pascal(n)
