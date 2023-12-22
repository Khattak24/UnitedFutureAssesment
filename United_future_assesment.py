# import pandas as pd

# # 2 : If I want to get a summary of categorical columns in a dataframe, how will I do that?

# # lets me define some data
# data = {
#     "Subjects" : ["Maths", "AI", "Data Science", "Programming"],
#     "Marks" : [95, 80, 90, 99]
# }

# df = pd.DataFrame(data)

# # now for getting summary there are builtin functions so i'll use describe() function
# categoricalSummary = df.describe(include='all')
# print(categoricalSummary)

# # 3 : What is difference between a function and a method?
# # function
# def print_name():
#     print("United Future")

# print_name()

# # Method
# class UnitedFuture:
#     def print_name(self):
#         print("United Future")

# unitedFuture = UnitedFuture()
# unitedFuture.print_name()




# 6. Given a list of integers: [1,2,4,5,6,8], the task is to implement the find_missing_num() function to determine and return the missing numbers?
# 1 : Pseudocode
"""
I'll use the list comprehension method because of memory efficent

Step 1 : First fine the mininmum and maximum number of the list
Step 2 : Iterate over the min and max using the range function
Step 3 : check in every iteration the number is present in th list or not if not it will append in the list
Step 4 : return the missing numbers
"""

# define the function
def find_missing_numbers(nums):
    # Step 1
    minNumber, maxNumber = min(nums), max(nums)

    # step 2 and 3
    missingNumbers = [num for num in range(minNumber, maxNumber + 1) if num not in nums]

    # step 4
    return missingNumbers

# define the list 
myList = [1,2,4,5,6,8]
missingNumbers = find_missing_numbers(myList)
print("Missing numbers are : " , missingNumbers)




