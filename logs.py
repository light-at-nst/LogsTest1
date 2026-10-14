from collections.abc import Sequence, Callable;

def readlogs(fp:str) -> list[str]:
    with open(fp, 'r') as file:
        return [line.rstrip('\n') for line in file.readlines()]


def writelogs(fp:str,group:Sequence[str],cl:bool=False) -> None:
    with open(fp, 'w' if cl else 'a', encoding='utf-8') as file:
        file.writelines(line.rstrip('\r\n')+'\n' for line in group)


def catlog(line:str,groups:dict[str,list[str]],types:Sequence[str]) -> dict[str,list[str]]:
    for t in types:
        if t in line:
            groups[t].append(line)
            break
    return groups   # return for easy chaining


def grouplogs(logs:Sequence[str],types:Sequence[str]) -> dict[str,list[str]]:
    groups={t:[] for t in types}
    for line in logs:
        catlog(line,groups,types)
    return groups

def grouplogsfromfile(fp:str,types:Sequence[str]) -> dict[str,list[str]]:
    groups={t:[] for t in types}
    with open(fp, 'r') as file:
        for line in file:
            catlog(line.rstrip('\n'),groups,types)
    return groups


def forgroupelem(group:list[str],do:Callable[[str],object]) -> None:
    for line in group: do(line)

