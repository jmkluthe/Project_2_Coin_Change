#!/usr/bin/env python3

import sys
from changegreedyalg import changegreedyalg
from changedp import changedp


def read_input(infilename):
    list_denoms = []
    amounts = []
    with open(infilename, 'r') as infile:
        lines = [line.rstrip('\r\n') for line in infile]
        for i in range(0, len(lines), 2):
            denoms = lines[i].split(" ")
            denoms = list(map(int, denoms))
            amount = int(lines[i+1])
            if denoms:
                list_denoms.append(denoms)
            if amount:
                amounts.append(amount)
    return list_denoms, amounts


def make_change_filename(infilename):
    parts = infilename.split('.')
    out_filename = parts[0] + "change.txt"
    return out_filename


def main():
    if not (len(sys.argv) > 0):
        print("You must supply a file for input.")
        exit(1)
    infilename = str(sys.argv[1])
    outfilename = make_change_filename(infilename)
    list_denoms, amounts = read_input(infilename)
    with open(outfilename, "w") as outfile:
        for index, denoms in enumerate(list_denoms):
            coins = changegreedyalg(denoms, amounts[index])
            outfile.writelines("\n".join(["Algorithm changegreedy:",
                                " ".join([str(el) for el in denoms]),
                                " ".join([str(el) for el in coins]),
                                str(sum(coins)),
                                "\n"]))
            # change 'changeslow' to make this run the dynamic algorithm
            coins = changedp(denoms, amounts[index])
        
            outfile.writelines("\n".join(["Algorithm changedp:",
                                 " ".join([str(el) for el in denoms]),
                                 " ".join([str(el) for el in coins]),
                                 str(sum(coins)),
                                 "\n"]))
            


if __name__ == "__main__":
    main()

