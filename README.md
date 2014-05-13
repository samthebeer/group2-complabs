group2-complabs
===============

this is the repository for codes and readmes written by group 2 of the third year theoretical comp lab 

MCMC GULP PROGRAM GROUP 2 SAMUEL ADAMS, HOLLY HATHRELL, ADAM MERCHANT, GATIS SEJA
this is group 2's program for finding the lowest energy configuration of an MgO CaO crystal using GULP

Automated running of MCMC to equilibrating the crystal. 
install Gulp version 4.0 from https://projects.ivec.org/gulp/
the eddited getmachine file we used for instaliation is in this repo

this readme assumes the programs are being run from terminal all in the directory gulp is installed in directory

1) run gulp_ingen.py by typing "python gulp_ingen.py"
2) create the initial input/output files by typing "./gulp<gulp_input>test.out" 
3) select number of swaps attempted by editing "run.py" and saving to working directory
the number of swaps preformed is the value of the variable "runs"
4)in terminal type "python run.py" this automatincaly preforms an equibrating run for the number of swaps selected
if runing correcty the terminal will print the percentage compleate and the run number as a guide to the user. 

gulp_ingenrand.py can be run in place of step one to start with a mixed crysal the amount of mixing can be tuned by changing number in  the if(r<number) in def isox(a,b,c,m):
