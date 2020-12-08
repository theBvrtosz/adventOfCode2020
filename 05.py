def get_input():
    with open('05.in', 'r') as f:
        return f.read().splitlines()

def find_seat_col(low, high, inp):
    for row in inp:
        mid = (low+high) // 2
        if row in ['F', 'L']:
            # get lower half
            high = mid
        else:
            # get upper half
            low = mid + 1
        if high == low:
            return high

def part1_solution(inp):
    
    answ = 0
    for boarding_pass in inp:
        row = find_seat_col(0,127,boarding_pass[:7])
        col = find_seat_col(0,7,boarding_pass[7:])
        seat_id = (row * 8) + col
        answ = max(answ, seat_id)
    return answ

if __name__ == "__main__":
    inp = get_input()
    print("part1 answer: {}".format(part1_solution(inp)))
