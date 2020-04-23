import random

with open('input.txt', 'w') as f:
    digit = [(random.randint(-1000000, 1000000)) for _ in range(50)]
    for e in digit:
        f.writelines('{}\n'.format(e))

import tempfile


def merge(first, second, result):
    first.seek(0)
    second.seek(0)
    result.seek(0)
    line_in_first, line_in_second = first.readline(), second.readline()
    while line_in_first and line_in_second:
        if int(line_in_first) > int(line_in_second):
            result.writelines(line_in_second)
            line_in_second = second.readline()
        elif int(line_in_first) < int(line_in_second):
            result.writelines(line_in_first)
            line_in_first = first.readline()
    if line_in_first:
        while line_in_first:
            result.writelines(line_in_first)
            line_in_first = first.readline()
    elif line_in_second:
        while line_in_second:
            result.writelines(line_in_second)
            line_in_second = second.readline()
    first.seek(0)
    second.seek(0)
    result.seek(0)


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def sort(input, output, size=10):
    if size < 0:
        raise Exception("size mast be positive")
    else:
        data = []
        temp_files = []
        merge_files = []
        with open(output, 'w') as out:
            with open(input) as input:
                word_count = 0
                line = input.readline()
                while line:
                    check = line[:-2]
                    if not is_number(check):
                        raise Exception("element mast be digit")
                    else:
                        data.append(int(line))
                        word_count += 1
                        if word_count == size:
                            temp = tempfile.NamedTemporaryFile(mode="w+")
                            temp_files.append(temp)
                            for line in sorted(data):
                                temp.writelines(str(line) + "\n")
                            temp.seek(0)
                            data.clear()
                            word_count = 0
                        line = input.readline()
                temp = tempfile.NamedTemporaryFile(mode="w+")
                temp_files.append(temp)
                for line in sorted(data):
                    temp.writelines(str(line) + "\n")
                temp.seek(0)
                data.clear()
                while len(temp_files) > 2:
                    while len(temp_files) > 1:
                        mergf = tempfile.NamedTemporaryFile(mode="w+")
                        merge(temp_files.pop(0), temp_files.pop(0), mergf)
                        merge_files.append(mergf)
                    if len(temp_files) == 1:
                        merge_files.append(temp_files.pop(0))
                    temp_files = merge_files[:]
                    merge_files.clear()
                if len(temp_files) == 2:
                    merge(temp_files.pop(0), temp_files.pop(0), out)
                else:
                    file = temp_files.pop(0);
                    line = file.readline()
                    while line: out.writelines(line)

