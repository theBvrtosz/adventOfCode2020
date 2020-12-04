import re

def parse_input(file_name):
    with open(file_name, 'r') as f:
        inp = [re.split(' |: | |-|\n',line) for line in f]
    return inp


def part1_solution(inp):
    password_list = []
    for minimum, maximum, lookup_char, password, _ in inp:
        char_count = password.count(lookup_char)
        password_meets_requirements = char_count >= int(minimum) and char_count <= int(maximum)
        if password_meets_requirements:
            password_list.append(password)
    print(len(password_list))



if __name__ == "__main__":
    inp = parse_input("02.in")
    part1_solution(inp)
    