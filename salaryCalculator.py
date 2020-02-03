import numpy as np
import os

'''
#constants
'''
number_of_days = 365
number_of_four_weeks = 13
number_of_weeks = 52
number_of_weeks_in_a_month = 4
hours_per_week = 40
options = [0,1,2,3]
program_Start = True

#input must be annual rate
def compute_salary_hourly(annual_amt):
    temp = annual_amt / number_of_weeks / hours_per_week
    return temp

#input must be hourly rate
def compute_salary_annual(hourly_amt):
    temp = hourly_amt * number_of_weeks * hours_per_week
    return temp

def display_output(hourly, weekly, monthly, yearly):
    print("""
    Hourly = {hr}
    weekly = {wk}
    Monthly = {mnth}
    Yearly = {yr}
    """.format(hr = hourly, wk = weekly, mnth = monthly, yr = yearly))

#test value
salary = 40000
instruction = """
Select number of corresponding salary type given:
1 = Hourly
2 = Annual
3 = Weekly
0 = Exit
"""

while(program_Start):
    print(instruction)
    selection = int(input("Select number corresponding to salary type given (or 0 to exit the program): "))

    if selection in options:

        if selection == 0:
            #stops the program from looping through the question again
            program_Start = False
            print("\nGoodbye! <3")
            break

        salary = int(input("Input Amount Given: "))

        #hourly is given
        if selection == 1:
            annual_salary = compute_salary_annual(salary)
            monthly_salary = annual_salary / number_of_four_weeks
            weekly_salary = monthly_salary / number_of_weeks_in_a_month
            display_output(salary, weekly_salary, monthly_salary, annual_salary)

        #annual is given
        elif selection == 2:
            hourly_salary = compute_salary_hourly(salary)
            monthly_salary = salary / number_of_four_weeks
            weekly_salary = monthly_salary / number_of_weeks_in_a_month
            display_output(hourly_salary, weekly_salary, monthly_salary, salary)

        #weekly is given
        elif selection == 3:
            hourly_salary = salary / hours_per_week
            annual_salary = compute_salary_annual(hourly_salary)
            monthly_salary = annual_salary / number_of_four_weeks
            display_output(hourly_salary, salary, monthly_salary, annual_salary)

    else:
        print("\nInvalid Input! Try Again...")

print("\n\n\n")
os.system("pause")
