import itertools
def main():
    print(list(itertools.permutations(range(10)))[999999]) #index starts at 0, so the 999,999 is the 1 millonth element
main()
