TREE = "#"

def parse_input(file_name):
    with open(file_name, 'r') as f:
        return f.read().splitlines()

def part1_solution(inp):
    counter=0
    for i in range(1, len(inp)):
        if inp[i][i*3%len(inp[i])] == TREE:
            counter += 1
    print(counter)

def part2_solution(inp):
    slopes = (
        (1,1),
        (3,1),
        (5,1),
        (7,1),
        (1,2)
    )
    prd = 1
    for right, down in slopes:
        counter=0
        for i in range(down, len(inp), down):
            if inp[i][int(i/down)*right%len(inp[i])] == TREE:
                counter += 1
        prd *= counter
    print(prd)
                

if __name__ == "__main__":
    inp = parse_input("03.in")
    part1_solution(inp)
    part2_solution(inp)
