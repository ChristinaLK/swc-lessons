import sys
import numpy as np

def main():
    assert len(sys.argv) > 1, "no argument given"
    action = sys.argv[1]
    filenames = sys.argv[2:]
    for f in filenames:
        data = np.loadtxt(f, delimiter=",")
        if action == '-max':
            for m in data.max(axis=1):
                print m
        elif action == '-min':
            for m in data.min(axis=1):
                print m
        else:
            print "wrong action"
		
main()