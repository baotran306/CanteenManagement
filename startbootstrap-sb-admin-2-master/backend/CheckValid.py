import datetime


def convert_date(date):
    try:
        date = date.strip()
        tmp = date.find(" ")
        if tmp != -1:
            dt, tm = date.split(" ")
            d, m, y = dt.split("/")
            new_form = y + "-" + m + "-" + d + " " + tm
            return new_form
        else:
            d, m, y = date.split("/")
            new_form = y + "-" + m + "-" + d
            return new_form
    except Exception as ex:
        print('----Error in conver_date----')
        print(ex)
        return False


def check_date(date):
    try:
        date = date.strip()
        if date != datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
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
            dt, tm = date.split(" ")
            if check_date(dt) and check_hms(tm):
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
