#!/usr/bin/env python3

from pathlib import Path
from collections import Counter
from logs import *

def getpath(rel:str) -> str:
    return str(Path(__file__).parent/rel)

def testgroups() -> dict[str,list[str]]:
    fp = getpath('c4-class-even/demo_logs.log')

    typs=('INFO','WARNING','DEBUG','ERROR')
    cats=tuple(map(lambda s: '['+s+']',typs))

    return grouplogsfromfile(fp,cats)

def testprint() -> None:
    groups=testgroups()
    sep='-'*50
    print(sep)
    print()
    for k in groups:
        forgroupelem(groups[k],lambda l: print(l,end='\n\n'))
        print(sep)
        print()

def testwrites() -> None:
    folder=getpath('logsout/demo')
    groups=testgroups()
    Path(folder).mkdir(parents=True,exist_ok=True)
    for k in groups:
        writelogs(f"{folder}/demo_{k[1:-1]}.log",groups[k],True)


def test1() -> None:
    fp=getpath('c5-class-morn/my-9-1s.log')
    logs=readlogs(fp)
    pos=7
    count=Counter()
    for line in logs:
        fields=line.split()
        if len(fields) > pos:
            count[fields[pos]] += 1
    print("Top5:\n")
    for item, n in count.most_common(5):
        print(item,n)

    

if __name__=='__main__':
    # testprint()
    # testwrites()
    test1()
