import argparse

parser = argparse.ArgumentParser(description='Script arguments')
parser.add_argument('file_path', help='Path to massive data')

args = parser.parse_args()
file_path = args.file_path


def solution(file_path):
    result = 0
    with open(file_path, 'r', encoding='utf-8') as in_file:
        data = in_file.readlines()
    data = sorted(int(i.strip()) for i in data)
    length = len(data)

    if length % 2:
        median = data[length // 2]
    else:
        median = round((data[length // 2] + data[length // 2 - 1]) / 2)

    for num in data:
        result += abs(median - num)
    return result


if __name__ == '__main__':
    try:
        result = solution(file_path)
        print(result)
    except Exception as err:
        print(err)