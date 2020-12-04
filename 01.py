def part1_solution(inp):
    for n in range(len(inp)):
        first_n = inp[n]
        lookup_n = 2020 - first_n
        if lookup_n in inp[n+1:]:
            return (first_n,lookup_n, n*lookup_n)

def part2_solution(inp):
    for n in range(len(inp)):
        first_n = inp[n]
        for second_n in inp[n+1:]:
            lookup_n = 2020-first_n-second_n
            if lookup_n in inp:
                return(first_n, second_n, lookup_n, first_n*second_n*lookup_n)


if __name__ == "__main__":
    with open("01.in", 'r') as f:
        inp = [int(line) for line in f]

    print("part1 {}".format(part1_solution(inp)))
    print("part2 {}".format(part2_solution(inp)))

    