# Python Practice Questions

# 1. Write a function that takes a temperature in Celsius and converts it to Fahrenheit
# Formula: (C × 9/5) + 32 = F
def celsius_to_fahrenheit(celsius):
    
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

# 2. Write a function that takes a list of numbers and returns a new list with only the numbers 
# that are divisible by 3
def divisible_by_three(numbers):
    divisible_by_three_list = []
    for number in numbers:
        if number % 3 == 0:
            divisible_by_three_list.append(number)
    return divisible_by_three_list

# 3. Write a function that takes a string and returns True if it's a palindrome, False if not
# (A palindrome reads the same forwards and backwards, like "radar" or "level")
def is_palindrome(text):
    reversed_text = text[::-1]
    return text == reversed_text

# 4. Write a function that takes two lists and returns a new list containing common elements
def find_common_elements(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)
    return common_elements

# 5. Write a function that takes a number and returns the sum of its digits
def sum_of_digits(number):
    digit_sum = sum(int(digit) for digit in str(number) if str(digit).isdigit())
    return digit_sum

if __name__ == "__main__":
    print("Fahrenheit:", celsius_to_fahrenheit(25))  # Example usage
    print("3'e bölünenler:", divisible_by_three([3,5,7,8,9,4,7,4,6,12,18,25]))  # Example usage
    print("Palindrome mi?", is_palindrome("radar"))  # Example usage
    print("Ortak elemanlar:", find_common_elements(["apple", "banana", "cherry"], ["banana", "kiwi", "apple"]))  # Example usage
    print("Rakamlar toplamı:", sum_of_digits(12345))  # Example usage

  