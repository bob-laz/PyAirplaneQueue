"""
Bob Laskowski
Compilers I
10/25/16
Snakes On A Plane

This is the Python class you invoke, along with an input file, if you wish to run this program from the command line. An
example call would be:

python Main.py input.txt

This class uses the first system argument, in the above example input.txt, as the input file for the program. See the
README for the proper input file format. This class creates a RequestProcess object using this input file and calls the
run method.
"""


import sys
import RequestProcess as RequestProcess

if __name__ == "__main__":
    rp = RequestProcess.RequestProcess(sys.argv[1])
    rp.run()

