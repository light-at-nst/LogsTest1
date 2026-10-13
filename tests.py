from pathlib import Path
from logs import grouplogsfromfile,forgroupelem

def testgroups() -> dict[str,list[str]]:
    fp = str(Path(__file__).parent/'c4-class-even/demo_logs.log')

    typs=('INFO','WARNING','DEBUG','ERROR')
    cats=tuple(map(lambda s: '['+s+']',typs))

    return grouplogsfromfile(fp,cats)

def testprint() -> None:
    groups=testgroups()
    sep='-'*50
    print(sep)
    print()
    for k in groups:
        forgroupelem(groups,k,lambda l: print(l,end='\n\n'))
        print(sep)
        print()

if __name__=='__main__':
    testprint()
