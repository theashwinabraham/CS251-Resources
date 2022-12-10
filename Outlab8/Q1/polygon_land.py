# IMPLEMENTED BY: ASHWIN ABRAHAM

def minCost(values):
    """
        This function accepts list
        It returns the result as cost.
    """
    if(len(values) == 3):
        return values[0]*values[1]*values[2]
    max_dex = 0
    for i in range(len(values)):
        if(values[i] > values[max_dex]):
            max_dex = i
    prev = max_dex - 1
    next = max_dex + 1
    if prev < 0:
        prev = len(values) - 1
    if next >= len(values):
        next = 0
    return values[prev]*values[max_dex]*values[next] + minCost(values[:max_dex]+values[max_dex+1:])

    


if __name__ == "__main__":
    import argparse
    CLI=argparse.ArgumentParser()
    CLI.add_argument("--values",  nargs="*",  type=int, default=[1, 2, 3])
    args = CLI.parse_args()
    print("values: %r" % args.values)
    cost = minCost(args.values)
    print(cost)