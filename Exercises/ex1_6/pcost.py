def portfolio_cost(filename: str) -> int:
    res = 0
    with open(filename, 'r') as f:
        for line in f:
            _, count, cost = line.strip().split()
            try:
                res += int(count) + float(cost)
            except ValueError as e:
                print("Couldn't parse:", line.strip())
                print('Reason:', e)

    return res

if __name__ == '__main__':
    print(portfolio_cost('../../Data/portfolio.dat'))