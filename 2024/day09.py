import sys

def parse(lines):
    nums = []
    for line in lines:
        for c in line.strip():
            nums.append(int(c))
        break
    return nums

def expand(nums):
    fill = True
    res = []
    i = 0
    for num in nums:
        for j in range(num):
            val = i if fill else -1
            res.append(val)
        fill = not fill
        if fill:
            i += 1
    return res

def compact(nums):
    # FIXME
    res = []
    l, r = 0, len(nums) - 1
    forward = True
    while l <= r:
        num = None
        if forward:
            num = nums[l]
            l += 1
            forward = num >= 0
        else:
            num = nums[r]
            r -= 1
            while num < 0 and l < r:
                num = nums[r]
                r -= 1
            forward = True
        if num >= 0:
            res.append(num)
    return res

def checksum(nums):
    total = 0
    for i in range(len(nums)):
        n = nums[i]
        if n < 0:
            break
        total += i * n
    return total

def exec(area):
    expanded = expand(nums)
    compacted = compact(expanded)
    return checksum(compacted)

# cat /path/to/input.txt | python day06.py
if __name__ == '__main__':
    nums = parse(sys.stdin)
    answer = exec(nums)
    print(answer)
