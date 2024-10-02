import json
import argparse

parser = argparse.ArgumentParser(description='Script arguments')
parser.add_argument('tests_path', help='Path to tests.json str format')
parser.add_argument('values_path', help='Path to values.json str format')
parser.add_argument('report_path', help='Path to report.json str format')

args = parser.parse_args()
tests_path = args.tests_path
values_path = args.values_path
report_path = args.report_path


def change_value(obj, values_dict):
    for el in obj:
        if 'value' in el:
            el['value'] = values_dict.get(el['id'], '')
        if el.get('values', []) != []:
            change_value(el['values'], values_dict)


def read_json(path, msg):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        raise FileNotFoundError(msg)
    except json.decoder.JSONDecodeError:
        raise json.decoder.JSONDecodeError('Wrong file format', '', 0)


def solution(tests_path, values_path, report_path, values_dict=None):
    if values_dict is None:
        values_dict = {}

    values_data = read_json(values_path, 'Values file not found, check file path')['values']
    for value in values_data:
        values_dict[value['id']] = value['value']

    report_objects = read_json(tests_path, 'Tests file not found, check file path')
    change_value(report_objects['tests'], values_dict)

    with open(report_path, 'w', encoding='utf-8') as report_file:
        json.dump(report_objects, report_file, indent=2)


if __name__ == '__main__':
    try:
        solution(tests_path, values_path, report_path)
        print('Success')
    except FileNotFoundError as err:
        print(err)
    except json.decoder.JSONDecodeError as err:
        print(err)
