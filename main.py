def line_to_dict(line):
    elements = line.split(" ")
    elem_split = [elem.split(":") for elem in elements]
    return {i[0]:i[1] for i in elem_split}


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


def passport_validator(dictionary):
    if all(k in dictionary for k in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")):
        return True
    return False


with open("input.txt") as file:
    data_lines = file.readlines()

data_in_dictionary_list = data_to_dict_list(data_lines)
valid_passport = 0
for dictionary in data_in_dictionary_list:
    if passport_validator(dictionary):
        valid_passport +=1

print(f"Total valid passports: {valid_passport}")