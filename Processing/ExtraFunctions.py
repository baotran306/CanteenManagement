import re


def check_type_customer(customer_type):
    if customer_type not in ['NO', 'YES']:
        print("----custome_type not acceptable in check_type_customer(just NO or YES)----")
        return False
    return True


def check_status_order(stt_order):
    if stt_order not in [0, 1, 2, 3]:
        print("----status order not acceptable in check_status_order(just 0, 1, 2)----")
        return False
    return True


def check_regex_password(your_pass):
    if " " in your_pass:
        print("----False Regex Password(Type 1)----")
        return False
    punctuation = "!\"#$%&'()*+,-/:;<=>?[\\]^`{|}~"
    for pun in punctuation:
        if pun in your_pass:
            print("----False Regex Password(Type 2)----")
            return False
    regex_type = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)[a-zA-Z\\d]{8,20}$"
    if re.search(regex_type, your_pass):
        return True
    print("----False Regex Password----")
    return False


def check_positive_number(num):
    if num < 0:
        print('----Deny negative number----')
        return False
    return True


def check_str_all_num(your_str):
    if your_str.isdigit():
        return True
    print('----Deny phone number or identity card contains character----')
    return False


def status_type(stt_type):
    if stt_type == 0:
        return "Chưa giao"
    elif stt_type == 1:
        return "Đã giao"
    elif stt_type == 2:
        return "Đang giao"
    else:
        return "Hủy"


def check_input_id_person(inp):
    try:
        if inp[:2].upper() == 'NV':
            if int(inp[2:]):
                return True
        if inp[:2].upper() == 'KH':
            if int(inp[2:]):
                return True
        return False
    except Exception as ex:
        print(ex)
        return False


def auto_generate_id_person(inp):
    # loi o day
    prefix = inp[:2]
    suffix = int(inp[2:])
    suffix += 1
    if suffix < 10:
        return prefix + "00" + str(suffix)
    elif suffix < 100:
        return prefix + "0" + str(suffix)
    else:
        return prefix + str(suffix)


# if __name__ == "__main__":
    # print(check_regex_password("AAAAAAAAAAa1"))
    # print(check_str_all_num('123aa'))
    # print(check_input_id_person('NV12a'))
