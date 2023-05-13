


def execute(tokens, straight=True, current=None, data=[], intdata=[], custom={}):

    if not straight:
        tokens = tokens[::-1]
    c = current if current else 0
    while c >= 0 and c < len(tokens):
        if tokens[c] == '"':
            c += 1
            while tokens[c] != '"':
                data.append(tokens[c])
                c += 1
        elif tokens[c] == '>':
            print(''.join(data))
            data = []
        elif tokens[c] == '<':
            data = list(input())
        elif tokens[c] == '!':
            c += 1
            link = []
            while tokens[c] != '!':
                link.append(tokens[c])
                c += 1
            return_data = [1, True, c]
            if link[0] == '0':
                return_data[2] = None
                link.pop(0)
            if '-' in link:
                return_data[1] = False
                return_data[0] = int(''.join(link)) * -1
            else:
                return_data[0] = int(''.join(link))
            return return_data
        elif tokens[c] == '#':
            intdata.append(int(''.join(data)))
            data = []
        elif tokens[c] == '$':
            for i in str(intdata.pop()):
                data.append(i)
        elif tokens[c] == '+':
            intdata[-1] += intdata[-2]
        elif tokens[c] == '-':
            intdata[-1] -= intdata[-2]
        elif tokens[c] == '*':
            intdata[-1] *= intdata[-2]
        elif tokens[c] == '/':
            intdata[-1] //= intdata[-2]
        elif tokens[c] == '%':
            intdata[-1] %= intdata[-2]
        elif tokens[c] == '^':
            intdata[-1] **= intdata[-2]
        elif tokens[c] == '&':
            intdata[-1] &= intdata[-2]
        elif tokens[c] == '|':
            intdata[-1] |= intdata[-2]
        elif tokens[c] == '.':
            data.pop()
        elif tokens[c] == ',':
            intdata.pop()
        elif tokens[c] == 'a':
            custom['a'] = intdata.pop()
        elif tokens[c] == 'b':
            custom['b'] = intdata.pop()
        elif tokens[c] == 'c':
            custom['c'] = intdata.pop()
        elif tokens[c] == 'd':
            custom['d'] = intdata.pop()
        elif tokens[c] == 'e':
            custom['e'] = data.pop()
        elif tokens[c] == 'f':
            custom['f'] = data.pop()
        elif tokens[c] == 'g':
            custom['g'] = data.pop()
        elif tokens[c] == 'h':
            custom['h'] = data.pop()

        elif tokens[c] == 'A':
            intdata.append(custom['a'])
        elif tokens[c] == 'B':
            intdata.append(custom['b'])
        elif tokens[c] == 'C':
            intdata.append(custom['c'])
        elif tokens[c] == 'D':
            intdata.append(custom['d'])
        elif tokens[c] == 'E':
            data.append(custom['e'])
        elif tokens[c] == 'F':
            data.append(custom['f'])
        elif tokens[c] == 'G':
            data.append(custom['g'])
        elif tokens[c] == 'H':
            data.append(custom['h'])
        elif tokens[c] == ' ':
            pass
        else:
            raise Exception('Invalid token: "{}"'.format(tokens[c]))
        c += 1

def run(string):
    d, i, c = [] , [], {}

    token_map = [list(i) for i in string.split('\n') if i]
    next_run = execute(token_map[0], straight=True, current=None, data=d, intdata=i, custom=c)
    while next_run != None:
        next_run = execute(token_map[next_run[0]-1], next_run[1], next_run[2], data=d, intdata=i, custom=c)

if __name__ == '__main__':
    string = '''
"abc"!0-2!
!30!>"fed"
......"1"#"0"#+++$>
'''
    run(string)