# Claire Francis, Feb 18, 2025, Week_5_python_2.py
# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as
import random
import numpy as np



#     247

# + 129

# ------

# The program should allow the student to enter the answer.
# If the answer is correct, a message of congratulations should be displayed.
# If the answer is incorrect a message showing the correct answer should be displayed.
# The program must use a function that accomplishes part of the needed tasks.





def get_answer():
    ######################
    num1 = random.randint(-1000000000, 1000000000)
    num2 = random.randint(-1000000000, 1000000000)
    sum = num1 + num2
    output = np.array([num1, num2, sum])
    ######################

    # Return the array to the calling function
    return output

if __name__ == '__main__':
    # Call kilometer_conversion, don't forget to pass in the kilometer parameter!
    variables = get_answer()
    number1 = variables[0]
    number2 = variables[1]
    result = variables[2]

    # Get User Input
    print(number1, ' + ', number2, ' = input your answer ')

    # Display the miles
    answer = int(input())
    if answer == result:
        print("Congratulations! Your answer is correct.")
    else:
        print("Sorry! Your answer is incorrect. The correct answer is: ", result)

