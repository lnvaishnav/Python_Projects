"""
Performing task to get all user inputs and their parts multiplication
"""
from math import pow as pow_
from time import sleep as sl
from functools import reduce
from os import sys

userInput_NumList = []
userInput_PartsList = []
userInput_DataArrangement = []

class UserInputPow:
    """
    This class UserInputPow is returning pow function as well as
    table structured data.
    """

    def __init__(self, num, parts):
        """
        init constructor takes two arguments and performs
        the further task.
        """
        self.num = num
        self.parts = parts
        self.pow_data = pow_(self.num, self.parts)

    def printing_asking_valuesandparts(self):
        """
        This function, printing_asking_valuesandparts() will print the user input
        number & its parts in table format.
        """
        return f"\t  {self.num}\t  {self.parts}\t {self.num * self.parts}\t  {self.pow_data}"

    def user_pow_fn(self):
        """
        This function, user_pow_fn() gets two integers and using pow function,
        it returns the its result.
        """
        return self.pow_data

def askingUserInput():
    """
    This function, askingUserInput() will ask user to input an integer for
    further actions with a warning.
    """
    print("\nNOTE: Read the rules, continued in 3 seconds... \
           \nKeep the range in mind after entering. \
           \nIf your limit crossed your input then you'll have to restart or exit thr program. \
           \nEx. If you entered 100 then it shouldn't be more than 100.\n")
    sl(3)
    askingUserInput.userInput = int(input("Enter a number: "))

    return askingUserInput.userInput

def askingValuesAndParts():
    """
    Function, askingValuesAndParts() performs certain tasks:

        1. userInput_num takes the number from user, Ex. 5 & userInput_parts takes total parts for
        no 5, ex. 3. And it means 5*3 = 15.
        2. userInput_numList & userInput_partsList will append the user input respectively,
        userInput_num & userInput_parts.
        3. If the userInput value comes to 1 or 0, then this function will be exit and further
        action will be executed.
        4. And if userInput goes below 0, then the program will ask user to terminate or re-start
        from very begining.
    """
    userInput = askingUserInput()
    print("Now, enter the number & total parts for the respective number.\n")
    while  userInput!= 0:
        userInput_Equality = 0
        userInput_num = int(input("Enter a number for partion: "))
        userInput_NumList.append(userInput_num)
        userInput_parts = int(input(f"Enter parts for {userInput_num}: "))
        userInput_PartsList.append(userInput_parts)

        userInput_Equality += (userInput_num * userInput_parts)
        userInput -= userInput_Equality
        print(f"Remaining input: {userInput}")
        if userInput == 1:
            break
        if userInput < 0:
            user_choice = int(input("The limit has gone in negative. \
                If you wanna continue, enter '1' else any key: "))
            if user_choice != 1:
                sys.exit(0)
            else:
                userInput_NumList.clear()
                userInput_PartsList.clear()
                return askingValuesAndParts()

def userInputNumPartsArrange():
    """
    Function, userInputNumPartsArrange() performs certain tasks:

        1. userInput_arrange will return a list of tuples includes the data which is arraged from
            userInput_numList and userInput_partsList.
        2. The all user input data will be shown in the table format with help of class
           UserInputPow's function, printing_asking_valuesandparts().
        3. userDataArranged_Sending will append the data which will be returned from class
            UserInputPow's function, user_pow_fn().
        4. userInput_FinalData uses reduce & lambda function to get the multiply of all the numbers.
        5. In the end, this function will show the very first user input and the final output.
    """
    print("\nYou're going to see your all inputs in 2 seconds...\n")
    sl(2)
    userInput_arrange = list(zip(userInput_NumList, userInput_PartsList))

    print("\tNumber\tParts\tTotal\tpow_data")
    for i in userInput_arrange:
        userDataArranged_Sending = UserInputPow(*i)
        userDataArranged_Sending_X = userDataArranged_Sending.user_pow_fn()

        print(userDataArranged_Sending.printing_asking_valuesandparts())
        userInput_DataArrangement.append(userDataArranged_Sending_X)
    userInput_FinalData = reduce(lambda x, y: x * y, userInput_DataArrangement)
    print(f"\nFinal Data:\t\t {askingUserInput.userInput} \t  {userInput_FinalData}")

if __name__ == "__main__":
    askingValuesAndParts()
    userInputNumPartsArrange()
 
