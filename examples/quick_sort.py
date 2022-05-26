import sys

sys.setrecursionlimit(1000000)


def qsort(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater


input_list = [1.2, 0.22, 0.43, 0.36, 0.39, 0.27, 100]
print('ORIGINAL LIST:')
print(input_list)
print('SORTED LIST:')
print(qsort(input_list))
