res = 0

with open('../../Data/portfolio.dat', 'r') as f:
    for line in f:
        _, count, cost = line.strip().split()
        res += int(count) + float(cost)

print(res)