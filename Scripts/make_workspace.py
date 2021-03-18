''' create the files and templates all at once so time does not need to be wasted creating files and copying templates. '''

import os
import sys
from time import sleep
import calendar
from datetime import date
import datetime
import my_functions as func

# specifically for trimont
# filename_base = "SOC Response Metrics"
# workspace_name = input("Enter the name of the workspace you are creating:\t")

func.clear_screen()

func.welcome_msg()

sleep(1)

func.clear_screen()

print("Verify this is the directory where you want to build your yearly workspace.\n")

sleep(1)

init_dir = os.getcwd()
print("Current directory:\n", init_dir)
sleep(1)

while True:
    answer = func.get_user_answer()
    if answer == 'y':
        print("Building workspace file structure now.")
        workspace_dir = init_dir
        break
    elif answer == 'n':
        print("\nPlease navigate to desired directory and try again.\n")
        sys.exit(0)
    else:
        print("\nInvalid entry, please enter (Y/y) or (N/n)")
        if answer == 'y' or 'n':
            break

sleep(.5)
func.clear_screen()

print("Building workspace in:\n", workspace_dir, '\n\n')

sleep(1)

func.clear_screen()

year = func.get_year()
year_int = int(year)

func.create_year_dir(year)

calendar_output = "calendar_year.txt"
year_calendar = calendar.calendar(year_int)
func.write_to_file(year_calendar, calendar_output)

month_order = func.id_number()
month_abbr = func.month_name()

week_list = func.minimum_month_weeks()

directory_list = [i + j for i, j in zip(month_order, month_abbr)]

print("The file structure is as follows:\n")

sleep(1.5)

for item in directory_list:
    min = 3
    func.check_dir_exists(item)
    os.chdir(item)
    print(item)
    month_no = directory_list.index(item) + 1
    week_list = func.create_week_list(year_int, month_no)
    for week in week_list:
        func.check_dir_exists(week)
        print('\t', week)
        week_list=week_list[:min]
    sleep(0.25)
    os.chdir('..')

sleep(0.5)

print("The workspace for the year", year_int, " is now complete.\n\n")
print("exiting program...")
sleep(2)
func.clear_screen()
sys.exit(0)
