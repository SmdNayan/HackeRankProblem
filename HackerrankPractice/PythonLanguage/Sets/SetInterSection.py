if __name__ == '__main__':
    n = int(input())
    sr1 = set(map(int, input().split(' ')))
    nc = int(input())
    sr2 = set(map(int, input().split(' ')))

    u = sr1.intersection(sr2)

    print(len(u))