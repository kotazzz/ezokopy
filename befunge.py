import random
def befunge93(program):
    height = len(program)
    weigth = len(program[0])

    prog_count = 0
    output = ''
    stack = []
    current = program[0][0]

    strmode = False
    location = [0, 0]
    direction = (0, 1)
    step = ()

    def safepop():
        if stack:
            return stack.pop()
        return 0

    while prog_count < 100000 and len(output) < 100:
        if strmode:
            if current == '"':
                strmode = False
            else:
                stack.append(ord(current))
        else:
            if current == '>':
                direction = (0, 1)
            elif current == '<':
                direction = (0, -1)
            elif current == 'v':
                direction = (1, 0)
            elif current == '^':
                direction = (-1, 0)
            elif current == '#':
                step = (direction[0] * 2, direction[1] * 2)
            elif current == '_':
                direction = (0, 1) if safepop() == 0 else (0, -1)
            elif current == '|':
                direction = (1, 0) if safepop() == 0 else (-1, 0)
            elif current == '+':
                stack.append(safepop() + safepop())
            elif current == '-':
                a, b = safepop(), safepop()
                stack.append(b - a)
            elif current == '*':
                stack.append(safepop() * safepop())
            elif current == '/':
                a, b = safepop(), safepop()
                stack.append(b // a)
            elif current == '%':
                a, b = safepop(), safepop()
                stack.append(b % a)
            elif current == '!':
                stack.append(int(safepop() == 0))
            elif current == '`':
                stack.append(int(safepop() < safepop()))
            elif current == ':':
                stack += [safepop()] * 2
            elif current == '\\':
                stack += [safepop(), safepop()]
            elif current == '$':
                safepop()
            elif current == '.':
                output += str(safepop()) + ' '
            elif current == ',':
                a = safepop()
                output += chr(a)
            elif current.isdigit():
                stack.append(int(current))
            elif current == '"':
                strmode = True
            elif current == '?':
                direction = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
            elif current == '@':
                break

        if step:
            location[0] += step[0]
            location[1] += step[1]
            step = ()
        else:
            location[0] += direction[0]
            location[1] += direction[1]

        location = [(height + location[0]) % height, (weigth + location[1]) % weigth]
        current = program[location[0]][location[1]]
        prog_count += 1

    return output
