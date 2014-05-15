group2-complabs
===============

this is the repository for codes and readmes written by group 2 of the third year theoretical comp lab 

MCMC GULP PROGRAM GROUP 2 SAMUEL ADAMS, HOLLY HATHRELL, ADAM MERCHANT, GATIS SEJA
this is group 2's program for finding the lowest energy configuration of an MgO CaO crystal using GULP

Automated running of MCMC to equilibrating the crystal. 
install Gulp version 4.0 from https://projects.ivec.org/gulp/
the eddited getmachine file we used for instaliation is in this repo

Necesary python scripts for this:
run.py
gulp_ingen.py
gulpgen.py
mcmc.py

This readme assumes the programs are being run from terminal and that the necesary python scripts are in the gulp src folder (where gulp is installed)

1) Edit gulp_ingen.py for the desired lattice dimensions, by default this is an 8*8*8 lattice
2) Edit the run.py variable "runs" for the proposed number of random swaps to consider, this is by default 200
3) in terminal type "python run.py"
run.py will print to terminal a percentage complete as a guide to the user

run.py can be edited to use gulp_ingenrand.py in place of gulp_ingen.py at line 11 in run.py to start with a mixed crysal the amount of mixing can be tuned by changing number in  the if(r<number) in def isox(a,b,c,m):

To visualise the results the necesarry python scripts are:
gulpgen.py
vca.py ~ for visulising only the calcium atoms
vmg.py ~ for visualising only the magnesium atoms
vis.py ~ for visualising both magnesium and calcium
NB calcium is seen as a yellow sphere, magnesium a white sphere


Steps are:
1)copy the "grid" file from the gulp src folder to another folder with the above python scripts
2)run gulpgen.py
3)run the desired visualisation script from above, the scene may be drastically zoomed out, if so zoom in to desired field of view
