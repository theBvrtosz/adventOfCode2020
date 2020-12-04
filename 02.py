import re

def parse_input(file_name):
    with open(file_name, 'r') as f:
        inp = [re.split('[- :]+', line) for line in f.read().splitlines()]
    return inp


def part1_solution(inp):
    correct_passwords = []
    for minimum, maximum, lookup_char, password in inp:
        char_count = password.count(lookup_char)
        if int(minimum) <= char_count <= int(maximum):
            correct_passwords.append(password)
    print(len(correct_passwords))


def part2_solution(inp):
    correct_passwords = []
    for first_position, second_position, lookup_char, password in inp:
        first_position_char = password[int(first_position)-1]
        second_position_char = password[int(second_position)-1]
        
        if (first_position_char == lookup_char) ^ (second_position_char == lookup_char):
            correct_passwords.append(password)

    print(len(correct_passwords))


if __name__ == "__main__":
    inp = parse_input("02.in")

    part1_solution(inp)
    part2_solution(inp)
    