import json
INPUT_FILE = "input.csv"


def csv_to_list_dict() -> list[dict]:
    with open(INPUT_FILE, 'r') as i_f:
        lines = i_f.read().split('\n')
        cells = [line.split(',') for line in lines]
        dicts = [dict(zip(cells[0], cells[i])) for i in range(1, len(lines)-1)]
    return dicts
    # TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(), indent=4))
#
