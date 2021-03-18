import os
import sys
from time import sleep
import calendar
from calendar import monthrange
import datetime
from datetime import date

def program_exit(code_block):
    try:
        code_block
    except KeyboardInterrupt:
        sys.exit(0)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_msg():
    welcome = "Welcome to the workspace creation wizard! This program creates a directory that makes a workspace encironment where files can be arranged by the time in which they were created. Separated by month, and week. \n\nExample: 'MAR\ 1 - 7'"

    print(welcome)

    sleep(1)

def write_to_file(content, out_file):
    with open(out_file, 'a') as f:
        print(content, file=f)

def get_user_answer():
    user_decision = input("\nConstruct here? (Y/n)\t")
    usr_decision = user_decision.lower()
    print(usr_decision)
    return usr_decision

def check_dir_exists(dir):
    exists = os.path.isdir(dir)
    if exists == False:
        os.mkdir(dir)

def list_directory():
    print('\n')
    print(os.listdir(os.getcwd()))
    print('\n')

def get_year():
    today = date.today()
    year = today.strftime("%Y")
    return year

def create_year_dir(year):
    check_dir_exists(year)
    os.chdir(year)

def month_name():
    mon_list = []
    i = 0
    for name in calendar.month_name:
        i = i + 1
        abbr = name[0:3]
        abbr = abbr.upper()
        mon_list.append(abbr)
    mon_list = mon_list[1:]
    # print(i)
    return mon_list

def id_number():
    IDs = []
    i = 1
    while i < 13:
        if i < 10:
            order = '0' + str(i) + '-'
        else:
            order = str(i) + '-'
        IDs.append(order)
        i = i+1
    return IDs

def create_month_dir(IDs, month_list):
    month_directories = []
    for i in range (0, 12):
        dir_name = IDs[i] + month_list[i]
        month_directories.append(dir_name)
        check_dir_exists(dir_name)
        return month_directories

def minimum_month_weeks():
    weeks = []
    week_one = "1-7"
    week_two = "8-14"
    week_three = "15-21"
    week_four = "22-28"

    weeks.append(week_one)
    weeks.append(week_two)
    weeks.append(week_three)
    weeks.append(week_four)

    return weeks

def create_week_list(year, month_no):
    count = 1
    week_list = minimum_month_weeks()
    count = count + 1
    days_num = number_of_days_in_month(year, month_no)
    if days_num >28:
        week_five = f"29-{days_num}"
        week_list.append(week_five)
    return week_list

def number_of_days_in_month(year, month):
    return monthrange(year, month)[1]
