from collections.abc import Sequence, Callable;

def grouplogs(fp:str,types:Sequence[str]) -> dict[str,list[str]]:
    groups={t:[] for t in types}
    with open(fp, 'r') as file:
        while (line := file.readline()):
            for c in types:
                if c in line:
                    groups[c].append(line)
                    break
    return groups


def forgroupelem(groups:dict,key:str,do:Callable[[str],object]) -> None:
    gr=groups[key]
    for line in gr: do(line)


def testgroups() -> dict[str,list[str]]:
    fp='c4-class-even/demo_logs.log'

    typs=('INFO','WARNING','DEBUG','ERROR')
    cats=tuple(map(lambda s: '['+s+']',typs))

    return grouplogs(fp,cats)

def testprint() -> None:
    groups=testgroups()
    sep='-'*50
    print(sep)
    print()
    for k in groups:
        forgroupelem(groups,k,print)
        print(sep)
        print()

testprint()
