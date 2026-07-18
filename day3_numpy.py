import numpy as np
print("--- Step 1 ---")
print("NumPy is ready!\n")

print("--- Step 2 ---")
my_list = [10, 20, 30, 40, 50]
my_array = np.array(my_list)
print("This is my NumPy array:", my_array, "\n")

print("--- Step 3 ---")
discounted_prices = my_array - 5
print("New prices after discount:", discounted_prices, "\n")

print("--- Step 4 ---")
total = np.sum(my_array)
average = np.mean(my_array)
print("The sum of all numbers is:", total)
print("The average of the numbers is:", average)
