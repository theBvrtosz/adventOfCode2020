import re

def parse_input(file_name):
    with open(file_name, 'r') as f:
        passports_raw = f.read().split('\n\n')
        passports = map(lambda x: re.split('[ \n]+', x), passports_raw)
        return list(passports)

def validate_byr(byr):
    return int(byr) in range(1920, 2003)

def validate_iyr(iyr):
    return int(iyr) in range(2010, 2021)

def validate_eyr(eyr):
    return int(eyr) in range(2020, 2031)

def validate_hgt(hgt):
    try:
        unit = hgt[-2:]
        number = int(hgt[:-2])

        if unit == 'cm':
            return number in range(150,194)
        elif unit == 'in':
            return number in range(59, 77)
        else:
            return False
    except ValueError:
        return False

def validate_hcl(hcl):
    validation_set = set('abcdef1234567890')
    first_char = hcl[0]
    validation_chars = hcl[1:].lower()
    hcl_len = len(hcl)

    return first_char == '#' and set(validation_chars).issubset(validation_set) and hcl_len == 7

def validate_ecl(ecl):
    return ecl in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

def validate_pid(pid):
    pid_len = len(pid)
    is_pid_numeric = pid.isnumeric()

    return pid_len == 9 and is_pid_numeric

def validate_passport(passport):
    mandatory_items = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])
    validation_dict = {
        'byr': validate_byr,
        'iyr': validate_iyr,
        'eyr': validate_eyr,
        'hgt': validate_hgt,
        'hcl': validate_hcl,
        'ecl': validate_ecl,
        'pid': validate_pid
    }

    present_items = set()
    valid_set = set()

    for field in passport:
        item, value = field.split(':')

        if item != 'cid':
            is_field_valid = validation_dict[item](value) 
            valid_set.add(is_field_valid)
            present_items.add(item)

    return valid_set == {True} and present_items == mandatory_items


def part1_solution(passports):
    mandatory_items = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])
    valid_passports_count = 0
    for passport in passports:
        items_present = set()
        for field in passport:
            passport_field = field.split(':')[0]
            items_present.add(passport_field)
        
        items_present.discard('cid')
        valid_passports_count += 1 if items_present == mandatory_items else 0
    return valid_passports_count

def part2_solution(passports):
    passport_count = 0
    for passport in passports:
        is_passport_valid = validate_passport(passport)
        passport_count += 1 if is_passport_valid else 0
    
    return passport_count


if __name__ == "__main__":
    passports = parse_input("04.in")
    print("part1 answer = {}".format(part1_solution(passports)))
    print("part2 answer = {}".format(part2_solution(passports)))
