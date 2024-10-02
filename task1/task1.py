import argparse
parser = argparse.ArgumentParser(description='Script arguments')
parser.add_argument('n', help='First arg')
parser.add_argument('m', help='Second arg')

args = parser.parse_args()
in_info = [args.n, args.m]


def solution(in_info):
    result = []
    try:
        n, m = [int(i) for i in in_info]
    except ValueError:
        raise ValueError('N and M must be integer')
    if n <= 0:
        raise ValueError('N must be > 0')
    if m <= 0:
        raise ValueError('M must be > 0')
    num = 1
    while True:
        result.append(num)
        num = 1 + (num + m - 2) % n
        if num == 1:
            return [str(i) for i in result]


if __name__ == '__main__':
    try:
        result = solution(in_info)
        print(''.join(result))
    except ValueError as err:
        print(err)