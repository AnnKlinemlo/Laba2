import json
with open("m.json", "r", encoding="utf-8") as read_file:
    data = json.load(read_file)


def sravn(arg):
    x = arg[0]
    if x in memory:
        if (arg[1] == memory[x]):
            return False
    return True


def op_and(arg):
    k = 0
    for i in range(0, len(arg)):
        if run(arg[i]) == False:
            k += 1
    if k == len(arg):
        return True
    if k > 0:
        return False

def op_or(arg):
    k = 0
    for i in range(0, len(arg)):
        if run(arg[i]) == False:
            k += 1
    if k > 1:
        return True
    else:
        return False


def pprint(arg):
    arg = ''.join(arg)
    print(arg)


memory = {
        "solution": 0,
        "skol": 0,
        "gnoy": 0,
        "temp": 0,
        "bol": 0,
        "otsutstvuey_zyb": 0,
        "zyb_mydrosti": 0,
        "chuvstvitelnost": 0,
        "yazva": 0,
        "krovotochenie": 0,
        "nalet": 0,
        "karies": 0,
        "zapah": 0,
        "svish": 0,
        "vospalenie": 0
        }


def get(arg):
    return memory[arg[0]]


def yes_or_no(arg):
    arg = ''.join(arg)
    answer = input(arg + ' (да/нет): ')
    return answer


def question_weather(arg):
    arg = ''.join(arg)
    answer = int(input(arg + ' (числовое значение): '))
    return answer


def op_set(arg):
    x = arg[0]
    for i in range(1, len(arg)):
        res = run(arg[i])
        if x in memory:
            if (res != None):
                memory[x] = res


def found(arg):
    x = arg[0]
    if x in memory:
        memory[x] = arg[1]


func = {'==': sravn,
        'print': pprint,
        'get': get,
        'yes_or_no': yes_or_no,
        'question_weather': question_weather,
        'and': op_and,
        'or': op_or,
        'set': op_set,
        'found': found
        }


def run(expression):  # обработка вложенных
    mas = []  # обработанные аргументы
    op = expression.get('op')
    func_1 = func.get(op)
    arg = expression.get('arg')
    for i in range(len(arg)):
        if isinstance(arg, dict):
            mas.append(run(arg[i]))
        else:
            mas.append(arg[i])
    return func_1(mas)


# Если левая часть правильная, то можем выполнить и правую.
for rule in data:
    if (run(rule['left']) == True):
        run(rule['right'])
