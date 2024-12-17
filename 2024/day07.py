import sys

def parse(lines):
    formulas = []
    for line in lines:
        token = line.split(':')
        test_val = int(token[0].strip())
        nums = token[1].strip().split(' ')
        formulas.append({'test': test_val, 'numbers': [int(n) for n in nums]})
    return formulas


def valid(test, nums):
    stack = []
    stack.append([0, nums[0]])
    while stack:
        i, val = stack.pop()
        if val > test:
            continue
        i += 1
        if i < len(nums):
            stack.append([i, val * nums[i]])
            stack.append([i, val + nums[i]])
        elif val == test:
            return True
    return False

def exec(formulas):
    total = 0
    for formula in formulas:
        test = formula['test']
        nums = formula['numbers']
        if valid(test, nums):
            total += test
    return total

# cat /path/to/input.txt | python day06.py
if __name__ == '__main__':
    formulas = parse(sys.stdin)
    answer = exec(formulas)
    print(answer)
