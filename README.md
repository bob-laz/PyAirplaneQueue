This is a program for our Compilers I class. It will simulate an airport take-off time slot manager. It is written in Python 3. 

This program requires an input file. You can edit the source to hard code your input file, then make the file executable. Preferably, you can call "python Main.py <input.txt/csv>" where the input file is a .txt or a .csv file in the following format:  

Delta 160, 0, 0, 4  
UAL 120, 0, 5, 4  
Delta 6, 2, 3, 6  

The following parameters are: request identifier, request submission time, time slot requested, length of time requested. Additional constraints on input include: the request identifier must be a string containing at least one character, the request submission time, time slot request and length of time requested values must be integers and the time slot requested must be greater than or equal to the request submission time. The program will not run and will instead display an error message if invalid input is passed in.