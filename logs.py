fp='c4-class-even/demo_logs.log'

types=('INFO','WARNING','DEBUG','ERROR')

cat=tuple(map(lambda s: '['+s+']',types))
groups={t:[] for t in cat}

with open(fp, 'r') as file:
    while (line := file.readline()):
        for c in cat:
            if c in line:
                groups[c].append(line)
                break


def grprint(key:str):
    if key[0]!='[' and key[-1]!=']':
        key='['+key+']'
    gr=groups[key]
    for line in gr:
        print(line)

# grprint('INFO')

sep='-'*50

for k in cat:
    print(sep)
    print()
    grprint(k)
print(sep)

