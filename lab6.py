#Lab 6: Python Lab 6 Problems
#Author: Annie Yung
#Date: 10/20/24

print("Problem 1: Basic Arithmetic and Input")

#defining function for math operations
def math_operations():
    #asks the user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate the sum, difference, product, and quotient
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2

    #check if the second number is zero before performing division to avoid division by zero
    if num2 != 0:
        quotient_result = num1 / num2
    else:
        quotient_result = "undefined (division by zero)"

    #print the results
    print(f"The sum of {num1} and {num2} is: {sum_result}")
    print(f"The difference of {num1} and {num2} is: {difference_result}")
    print(f"The product of {num1} and {num2} is: {product_result}")
    print(f"The quotient of {num1} and {num2} is: {quotient_result}")


#main function
math_operations()

print()
print()

print("Problem 2: Temperature Converter")

#defining function to convert temperature from C to F and vice versa
def convert_temperatures(temp, unit):
    if unit == 'C':
        #convert Celsius to Fahrenheit
        fahrenheit = (temp * 9/5) + 32
        return fahrenheit
    elif unit == 'F':
        #convert Fahrenheit to Celsius
        celsius = (temp - 32) * 5/9
        return celsius
    else:
        #return an error message if there's an invalid unit
        return "Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit."

#asks the user to input temperature and unit
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit that you want to convert the temperature to ('C' for Celsius or 'F' for Fahrenheit): ").upper()

result = convert_temperatures(temperature, unit)
print(f"The converted temperature is: {result}")

print()
print()

print("Problem 3: List Manipulation")
user_input = input("Please enter a list of numbers separated by commas: ")

#splits input into a list
number_list = [int(number) for number in user_input.split(', ')]

#will get the maximum & minimum, sum of numbers, and will sort list in ascending order
max_num = max(number_list)
min_num = min(number_list)
sum_of_nums = sum(number_list)
sorted_list = sorted(number_list)

#prints the results
print(f"Maximum number: {max_num}")
print(f"Minimum number: {min_num}")
print(f"Sum of all numbers: {sum_of_nums}")
print(f"Sorted list in ascending order: {sorted_list}")

print()
print()

print("Problem 4: String Reversal")
def reverse_string(input_string):
    return input_string[::-1]

result = reverse_string("hello")
print(result)

print()
print()

print("Problem 5: Factorial Calculation")
#defining function to calculate a factorial
def calculate_factorial(n):
  if n == 0 or n == 1:
      return 1
  else:
      return n* calculate_factorial(n-1)

#prints out the factorial of 7 as an example
print(calculate_factorial(7))

print()
print()

print("Problem 6: Prime Number Checker")
def is_prime(n):
    #check if n is less than 2
    if n < 2:
        return False
        # check for factors from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#user input
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

print()
print()

print("Problem 7: Dictionary of Word Frequencies ")
def frequency_words():
    #asks the user to insert a sentence
    sentence = input("Enter a sentence: ")

    #splits the sentence into words
    words = sentence.split()

    #creates an empty dictionary that will store the frequencies of the words
    word_count = {}

    #loops through each word in the list of words
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print(word_count)

frequency_words()
