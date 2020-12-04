import re

with open("input.txt") as file:
    data_lines = file.readlines()


def line_to_dict(line):
    elements = line.split(" ")
    elem_split = [elem.split(":") for elem in elements]
    return {i[0]: i[1].replace("\n", "") for i in elem_split}


def data_to_dict_list(data):
    dict_list = [{}]
    current_line = 0
    for line in data:
        if line == '\n':
            dict_list.append({})
            current_line += 1
        else:
            dict_list[current_line] = {**dict_list[current_line], **line_to_dict(line)}
    return dict_list


def passport_field_checker(dictionary):
    if all(k in dictionary for k in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")):
        return True
    return False


data_in_dictionary_list = data_to_dict_list(data_lines)
passports_checked = []
for dictionary in data_in_dictionary_list:
    if passport_field_checker(dictionary):
        passports_checked.append(dictionary)

print(f"Total checked passports: {len(passports_checked)}")


#Part Two
def validate_birthday(byr):
    return 1920 <= int(byr) <= 2002


def validate_issue_year(iyr):
    return 2010 <= int(iyr) <= 2020


def validate_expiration_year(eyr):
    return 2020 <= int(eyr) <= 2030


def validate_height(hgt):
    cm_regex = re.compile(r'^[0-9]{3}cm$')
    in_regex = re.compile(r'^[0-9]{2}in$')
    if "cm" in hgt:
        if not re.match(cm_regex, hgt):
            return False
        if 150 <= int(hgt[:3]) <= 193:
            return True
    if "in" in hgt:
        if not re.match(in_regex, hgt):
            return False
        if 59 <= int(hgt[:2]) <= 76:
            return True
    return False


def validate_hair_color(hcl):
    hcl_regex = re.compile(r'^#[0-9a-f]{6}$')
    return re.match(hcl_regex, hcl)


def validate_passport_id(pid):
    pid_regex = re.compile(r'^[0-9]{9}$')
    return re.match(pid_regex, pid)


def validate_eye_color(ecl):
    eye_colors = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    return ecl in eye_colors


def passport_field_checker(passport):
    return all([
        validate_birthday(passport["byr"]),
        validate_expiration_year(passport["eyr"]),
        validate_issue_year(passport["iyr"]),
        validate_height(passport["hgt"]),
        validate_hair_color(passport["hcl"]),
        validate_passport_id(passport["pid"]),
        validate_eye_color(passport["ecl"])]
    )


valid_passports = 0

for passport in passports_checked:
    if passport_field_checker(passport):
        valid_passports += 1

print(f"Total valid passports: {valid_passports}")