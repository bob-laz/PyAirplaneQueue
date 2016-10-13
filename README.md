This is a program for our Compilers I class. It will simulate an airport take-off time slot manager. It is written in Python 3. 

This program requires an input file. You can edit the source to hard code your input file, then make the file executable. Preferably, you can call "python <filename.py> <input.txt>"

The input file should be a text file in the following format:
Delta 160, 0, 0, 4, x, x \n
UAL 120, 0, 5, 4, x, x \n 
Delta 6, 2, 3, 6, x, x \n

The following parameters are: request identifier, request submission time, time slot requested, length of time requested, actual start time, actual end time. The last two slots, currently x's, will be updates when the program is run. 