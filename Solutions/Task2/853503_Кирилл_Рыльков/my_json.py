
BRACKET=['{','}','[',']']
COLON = ":"
COMMA = ","

LITERALS=["true","false","null"]

CONTROL_CHARACTER = [' ', '\t', '\b', '\n']
QUOTATION_MARK = "\""

DIGITS =['1','2','3','4','5','6','7','8','9','0']
MINUS = '-'
PLUS = '+'
EXP = ['E', 'e']
POINT = '.'


def lex(string):
    tokens = []
    while len(string):
        if string[0] in (DIGITS + [MINUS, PLUS, POINT] + EXP):
            value = ""
            for c in string:
                if c in (DIGITS + [MINUS, PLUS, POINT] + EXP):
                    value += c
                else:
                    break
            string = string[len(value):]
            if "." in value:
                value = float(value)
            else:
                value = int(value)
            tokens.append(value)
            continue
        if string[0] == QUOTATION_MARK:
            string = string[1:]
            value = ""
            for c in string:
                if c == QUOTATION_MARK:
                    string = string[len(value) + 1:]
                    tokens.append(value)
                    break
                value += c
            continue
        if string[:len(LITERALS[1])] == LITERALS[1]:
            tokens.append(False)
            string = string[len(LITERALS[1]):]
            continue
        if string[:len(LITERALS[0])] == LITERALS[0]:
            tokens.append(True)
            string = string[len(LITERALS[0]):]
            continue
        if string[:len(LITERALS[2])] == LITERALS[2]:
            tokens.append(None)
            string = string[len(LITERALS[2]):]
            continue
        if string[0] in (BRACKET+[COLON,COMMA]):
            tokens.append(string[0])
            string = string[1:]
            continue
        if string[0] in CONTROL_CHARACTER:
            string = string[1:]
            continue
    return tokens


def parse_object(tokens):
    obj = {}
    if tokens[0] == BRACKET[1]:
        return obj, tokens[1:]
    while True:
        key = tokens[0]
        if type(key) is str:
            tokens = tokens[1:]
        value, tokens = parse(tokens[1:], False)
        obj[key] = value
        if tokens[0] == BRACKET[1]:
            return obj, tokens[1:]
        tokens = tokens[1:]


def parse_array(tokens):
    array = []
    if tokens[0] == BRACKET[3]:
        return array, tokens[1:]
    while True:
        value, tokens = parse(tokens, first = False)
        array.append(value)
        if tokens[0] == BRACKET[3]:
            return array, tokens[1:]
        else:
            tokens = tokens[1:]


def parse(tokens, first):
    token = tokens[0]
    if first and token != BRACKET[0]:
        raise Exception('the object must begin with expected curly bracket')
    if token == BRACKET[0]:
        return parse_object(tokens[1:])
    elif token == BRACKET[2]:
        return parse_array(tokens[1:])
    else:
        return token, tokens[1:]


def get_array(array):
    string = '['
    if len(array) == 0:
        return '[]'

    for item in array:
        if type(item) is dict:
            string += get_object(item)
        elif type(item) is list:
            string += get_array(item)
        elif type(item) is str:
            string += QUOTATION_MARK + item + QUOTATION_MARK
        elif item is None:
            string += LITERALS[2]
        elif item is True:
            string += LITERALS[0]
        elif item is False:
            string += LITERALS[1]
        elif type(item) is int or float:
            string += str(item)
        if array.index(item) != len(array) - 1:
            string += ', '
    return string + ']'


def get_object(object):
    string = '{'
    if len(list(object.keys())) == 0:
        return '{}'

    for item in object:
        if type(object[item]) is dict:
            string += '"' + str(item) + '": ' + get_object(object[item])
        elif type(object[item]) is list:
            string += '"' + str(item) + '": ' + get_array(object[item])
        elif type(object[item]) is str:
            string += '"' + str(item) + '": ' + '"' + object[item] + '"'
        elif object[item]:
            string += '"' + str(item) + '": ' + "true"
        elif object[item] is None:
            string += '"' + str(item) + '": ' + "null"
        elif not object[item]:
            string += '"' + str(item) + '": ' + "false"
        if list(object.keys()).index(item) != len(list(object.keys())) - 1:
            string += ', '
    return string + '}'


def from_json(string):
    tokens = lex(string)
    return parse(tokens, True)[0]


def to_json(object):
    return get_object(object)
