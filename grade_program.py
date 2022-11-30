#!/usr/bin/env python3

# Created by: Nathan Araujo
# Created on: November 26, 2022
# This program asks the user for their level, it then turns that level into a percentage, it then displays it back to the user


# This functions determines the user percentage from the level they entered
def calc_level(level):
    # Declare percentage to 0
    percentage = 0

    # Finds the percentage value of the inputted level
    match level:
        case "4+":
            percentage = 96
        case "4":
            percentage = 90
        case "4-":
            percentage = 84
        case "3+":
            percentage = 78
        case "3":
            percentage = 74
        case "3-":
            percentage = 71
        case "2+":
            percentage = 68
        case "2":
            percentage = 64
        case "2-":
            percentage = 61
        case "1+":
            percentage = 58
        case "1":
            percentage = 54
        case "-1":
            percentage = 51
        case _:
            percentage = -1

    # Returns percentage value to main()
    return percentage


def main():
    # Asks user for their level
    user_level = input("Enter your percentage: ")

    # Calls calc_level
    percentage = calc_level(user_level)

    # If the percentage is equal to -1 then display invalid input
    if percentage == -1:
        print(f"{user_level} is not valid input")
    else:
        # Displays the percentage of the level to the user
        print(f"Your level {user_level} is equal to {percentage}%")


if __name__ == "__main__":
    main()
