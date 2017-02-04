#!/usr/bin/env python3

import sys
from changegreedyalg import changegreedyalg
from changeslow import changeslow


def read_input(infilename):
    # open(infilename, "r")
    with open(infilename, 'r') as infile:
        lines = [line.rstrip('\r\n') for line in infile]
        denoms = lines[0].split(" ")
        denoms = list(map(int, denoms))
        amount = int(lines[1])
    return denoms, amount


def make_change_filename(infilename):
    parts = infilename.split('.')
    out_filename = parts[0] + "change.txt"
    return out_filename


def main():
    if not (len(sys.argv) > 0):
        print("You must supply a file for input.")
        exit(1)
    infilename = "sampleinputfile2.txt"#str(sys.argv[1])
    outfilename = make_change_filename(infilename)
    denoms, amount = read_input(infilename)
    with open(outfilename, "w") as outfile:
        coins = changeslow(denoms, amount)
        outfile.writelines([str(el) for el in ["Algorithm changeslow:", denoms, coins, sum(coins), "\n"]])
        coins = changegreedyalg(denoms, amount)
        outfile.writelines([str(el) for el in ["Algorithm changegreedy:", denoms, coins, sum(coins), "\n"]])


if __name__ == "__main__":
    main()