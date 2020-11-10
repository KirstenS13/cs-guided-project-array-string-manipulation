"""
You are given a non-empty array that represents the digits of a non-negative integer.

Write a function that increments the number by 1.

The digits are stored so that the digit representing the most significant place value is at the beginning of the array. Each element in the array only contains a single digit.

You will not receive a leading 0 in your input array (except for the number 0 itself).

Example 1:

Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.

Example 2:

Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.

Example 3:

Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""
def plus_one(digits):
#     # Your code here
#     for i in range(len(digits), 0, -1):
#         print(i)

# print(plus_one([1, 2, 3]))

    # UNDERSTAND
    # add one to the last number if it's not a 9
    # if it is a 9, make it a 0, and then repeat with the second to last numbre
    # if the number is a 9:
    #   make it 0, and repeat with previous number
    # else if it's not a 9:
    #   add 1
    # if we get the the first number and it's a 9, make it a 10


    # PLAN
    # index = len(digits)
    # loop until: the current number is not 9
    #   if the number is a 9:
    #       make it zero, and repeat w/ previous number
    #       set digits[i] to 9
    #   else if it's not a 9:
    #       add 1 to digits[i]
    #   decrement index
    # if we get to the first number (index == 0) and it's a 9, make it a 10 (insert 1 at the 0th index, make 1st index 0)

    index = len(digits) - 1
    while index >= 0 and digits[index] == 9:
        digits[index] = 0
        index = index - 1

    if index == -1:
        digits.insert(0, 1)
    else:
        digits[index] += 1

    return digits


print(plus_one([1, 2, 3]))