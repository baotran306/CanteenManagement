import datetime
from datetime import datetime as dt


def convert_date(date):
    try:
        date = date.strip()
        tmp = date.find(" ")
        if tmp != -1:
            date_split, time_split = date.split(" ")
            d, m, y = date_split.split("/")
            new_form = y + "-" + m + "-" + d + " " + time_split
            return new_form
        else:
            d, m, y = date.split("/")
            new_form = y + "-" + m + "-" + d
            return new_form
    except Exception as ex:
        print('----Error in convert_date----')
        print(ex)
        return False


def check_date(date):
    try:
        date = date.strip()
        if date != datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
        print("----Wrong Format Date in check_date----")
        return False


def check_hms(time):
    try:
        time = time.strip()
        h, m, s = time.split(":")
        check = 0
        if 0 <= int(h) <= 23:
            check += 1
        if 0 <= int(m) <= 59:
            check += 1
        if 0 <= int(s) <= 59:
            check += 1
        if check == 3:
            return True
        else:
            return False
    except Exception as ex:
        print('----Error in check_hms----')
        print(ex)
        return False


def check_format_datetime(date):
    try:
        date = date.strip()
        tmp = date.find(" ")
        if tmp != -1:
            date_split, time_split = date.split(" ")
            if check_date(date_split) and check_hms(time_split):
                return True
            else:
                print('format_datetime is false: yyyy-mm-dd hh:mm:ss')
                return False
        else:
            if check_date(date):
                return True
            else:
                print('format_datetime is false: yyyy-mm-dd hh:mm:ss')
                return False
    except Exception as ex:
        print('----Error in check_format_datetime----')
        print(ex)
        return False


def check_limit_time(time_inp):
    now = dt.now()
    if str(now) < time_inp:
        print('----Deny time input greater than time now----')
        return False
    return True


def check_start_end_time(time_start, time_end):
    if time_start > time_end:
        print('----Deny time start greater than time end----')
        return False
    return True


def get_session_day_menu(time_day):
    time_day = time_day.strip()
    _, time = time_day.split(" ")
    hour = time[:2]
    if int(hour) < 10:
        return "Buổi sáng"
    elif int(hour) < 16:
        return "Buổi trưa"
    else:
        return "Buổi chiều"
    pass


# print(str(dt.now()) > "2020-08-15 04:06:00")
