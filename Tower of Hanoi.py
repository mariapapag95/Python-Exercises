def hanoi(n):
    hanoi(n, start='peg 1', destination='peg 2', spare='peg 3')
    print ("Move a disk from {} to {}.".format(start, destination)