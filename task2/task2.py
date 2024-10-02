import argparse

parser = argparse.ArgumentParser(description='Script arguments')
parser.add_argument('circle_file', help='Path to file with circle parametrs')
parser.add_argument('dots_file', help='Path to file with dots coordinates')

args = parser.parse_args()
circle_file = args.circle_file
dots_file = args.dots_file


def solution(circle_file, dots_file):
    with open(circle_file, 'r', encoding='utf-8') as circle_data:
        x, y = map(int, circle_data.readline().strip().split())
        radius = int(circle_data.readline())
        if radius < 1:
            raise ValueError('Radius must be > 0')

    with open(dots_file, 'r', encoding='utf-8') as dots_data:
        for dots in dots_data:
            dot_x, dot_y = map(int, dots.strip().split())
            result = (dot_x - x)**2 + (dot_y - y)**2

            if result == radius**2:
                print(0)
            elif result < radius**2:
                print(1)
            else:
                print(2)


if __name__ == '__main__':
    try:
        solution(circle_file, dots_file)
    except Exception as err:
        print(err)
