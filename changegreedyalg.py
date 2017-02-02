#!/usr/bin/python
import sys
"""
usage: first command line argument should be the input filename
"""

def changegreedyalg(denoms, amount):
	numcoins = [0]*(len(denoms))
	#print len(numcoins)
	#uniquecoins = len(denoms)
	for i in range (len(denoms)-1, -1, -1):

		while denoms[i] <= amount:
			amount = amount - denoms[i]
			numcoins[i] = numcoins[i]+1
			
	return numcoins


inputfilename = str(sys.argv[1])
#print inputfilename
inputfile = open(inputfilename, "r")
lines = [line.rstrip('\r\n') for line in open(inputfilename)]

denoms = lines[0].split(" ")
denoms = list(map(int, denoms))


amount = int(lines[1])
#print denoms
#print amount


numcoins = changegreedyalg(denoms, amount)
totalcoins = sum(numcoins)
print numcoins
print totalcoins


